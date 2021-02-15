from django.shortcuts import render, redirect
from rest_framework import generics, status, views
from rest_framework.response import Response
from .serializers import RegisterSerializer, EmailVerificationSerializer, LoginSerialiser
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class RegisterView(generics.GenericAPIView):
    """ register user class, POST request """
    
    serializer_class = RegisterSerializer
    
    def post(self, request):
        """ post request + creating token """
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        user_data = serializer.data
        
        user = User.objects.get(email=user_data['email'])
        
        token = RefreshToken.for_user(user).access_token
        
        current_site = get_current_site(request).domain
        
        relativeLink = reverse('email-verify')
        
        absurl = 'http://'+current_site+relativeLink+'?token='+str(token)
        
        email_body = 'Salut '+user.username+'\nutilise le lien ci-dessous pour vérifier ton adresse email: \n'+absurl
        
        data = {'email_body': email_body, 'email_to': user.email,'email_subject': 'verify your email'}
        
        Util.send_email(data)
        
        return Response(user_data, status=status.HTTP_201_CREATED)
    
class VerifyEmail(views.APIView):
    """ class to verify user """
    serializer_class = EmailVerificationSerializer
    
    token_param_conf = openapi.Parameter('token', in_=openapi.IN_QUERY, description='description', type=openapi.TYPE_STRING)
    
    @swagger_auto_schema(manual_parameters=[token_param_conf])
    def get(self, request):
        """ get request """
        token=request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user=User.objects.get(id=payload['user_id'])
            
            if not user.is_verified:
                user.is_verified = True
                user.save()
            # return Response({'email': 'successfully activated'}, status=status.HTTP_200_OK)
            return redirect('https://pur-beurre-front.herokuapp.com/')
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'activation link expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'invalid token'}, status=status.HTTP_400_BAD_REQUEST)
    
    
class LoginAPIView(generics.GenericAPIView):
    """ login a user, post request """
    
    serializer_class = LoginSerialiser
    
    def post(self, request):
        """ post request, checking if user is valid (email verification) """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)