from django.shortcuts import render
"""
Views for the user API
"""
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer
from rest_framework import  permissions, viewsets, generics, permissions


from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer

from django.contrib.auth import authenticate

from rest_framework.authentication import (
    BasicAuthentication,SessionAuthentication,TokenAuthentication
)

from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


class UserView(generics.CreateAPIView):
    
    serializer_class = UserSerializer
    
    



