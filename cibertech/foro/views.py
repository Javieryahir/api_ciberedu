from django.shortcuts import render
from rest_framework import  permissions, viewsets, generics, permissions
from rest_framework import generics
from .models import Category, Message, UsersM
from .serializers import categorySerializers, messageSerializers, categoryMessageSerializers
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class categoryListView(generics.ListAPIView , generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = categorySerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user_instance = UsersM.objects.get(username=self.request.user.username)
        serializer.save(createdBy=user_instance)

        serializer.save(nameCreator=self.request.user.username)

class messagesbyCategoryListView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    lookup_url_kwarg = 'CategoryId'
    serializer_class = categoryMessageSerializers

class messageListView(generics.ListAPIView, generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = messageSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user_instance = UsersM.objects.get(username=self.request.user.username)
        serializer.save(createdBy=user_instance)

        serializer.save(nameCreator=self.request.user.username)