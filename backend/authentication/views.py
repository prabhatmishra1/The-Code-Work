from django.http import request
from django.shortcuts import render
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model  # If used custom user model
from .serializers import *
from . utils import send_otp
# Create your views here.


class UserLoginView(APIView):
    '''Check user credential'''
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, reqeust, *agrs, **kwargs):
        email = reqeust.data.get("email")
        password = reqeust.data.get("password")
        user = authenticate(email=email, password=password)
        if user:
            print(user.code)
            if send_otp(user.mobile, user.code):
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Valid User OTP has been sent',
                }
                return Response(response)
            else:
                return Response({"message": "OTP can't send"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': "invalid credentail"}, status=status.HTTP_401_UNAUTHORIZED)


class VerifyOTPView(TokenObtainPairView):
    '''Verify otp and send JWT tokens'''

    def post(self, request, *args, **kwargs):
        if request.data.get("code") and request.data.get("email"):
            user = UserModel.objects.get(email=request.data.get("email"))
            print(user)
            if user:
                code = user.code
                print(user, code)
                if str(code) == request.data.get('code'):
                    code.save()
                    #login(request, user)
                    data = {}
                    refresh = TokenObtainPairSerializer.get_token(user)
                    data['refresh'] = str(refresh)
                    data['access'] = str(refresh.access_token)
                    return Response(data, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "Server Error"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "please enter OTP"}, status=status.HTTP_400_BAD_REQUEST)


class CreateUserView(generics.CreateAPIView):
    '''User Signup View'''
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer


class Homepageview(APIView):
    '''Profile Page'''
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({"username": request.user.email})
