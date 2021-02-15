from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken
import json

class UserManager(BaseUserManager):
    """which query sets we can run """
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Please provide an username')
        if email is None:
            raise TypeError('Please provide an email')
        user=self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, username, email, password=None):
        """creating super user with the create_user method"""
        if password is None:
            raise TypeError('Password can not be none')
        
        user=self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    """model class"""
    username = models.CharField(max_length=100, unique = True, db_index=True)
    email = models.EmailField(max_length=100, unique = True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # password = models.CharField(max_length=100)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        
        res_token = {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }
        
        return json.dumps(res_token)