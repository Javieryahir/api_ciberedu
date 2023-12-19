from django.shortcuts import render
from rest_framework import  permissions, viewsets, generics, permissions
from rest_framework import generics
from .models import BlogPost, UsersM
from .serializers import frontBlogSerializers, contentBlogSerializers
from rest_framework.permissions import IsAuthenticated
# Create your views here.
# Create your views here.
class frontBlogListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = frontBlogSerializers

class contentBlogListView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    lookup_url_kwarg = 'BlogId'
    serializer_class = contentBlogSerializers

class BlogListView( generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = contentBlogSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
 
        user_instance = UsersM.objects.get(username=self.request.user.username)
        serializer.save(createdBy=user_instance)

        serializer.save(nameCreator=self.request.user.username)

