from rest_framework import serializers
from authentication.models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
        
class RegisterSerializer(serializers.ModelSerializer):
    """ serializers for registration """
    
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        
    def validate(self, attrs): 
        """ method to validate user informations """
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        
        if not username.isalnum():
            raise serializers.ValidationError('the username should contain alpha num characters')
        
        return attrs
    
    def create(self, validated_data):
        """ create method that is called when we use serializer.save() """
        return User.objects.create_user(**validated_data)
    
class EmailVerificationSerializer(serializers.ModelSerializer):
    """ email verification serializers """
    token = serializers.CharField(max_length=555)
    
    class Meta:
        model = User
        fields = ['token']

class LoginSerialiser(serializers.ModelSerializer):
    """ login serializers """
    
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3, read_only=True)
    tokens = serializers.CharField(max_length=255, min_length=6, read_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']
    
    def validate(self, attrs):
        """ method to validate user informations """
                
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        
        user = auth.authenticate(email=email, password=password)
        
        if not user:
            raise AuthenticationFailed('invalid informations, try again')
        
        if not user.is_active:
            raise AuthenticationFailed('no account, contact support')
        
        if not user.is_verified:
            raise AuthenticationFailed('email not verified')
        
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }
        
        return super().validate(attrs)