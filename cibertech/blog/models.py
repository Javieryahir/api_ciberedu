from django.db import models
from user.models import UsersM 

# Create your models here.

class BlogPost(models.Model):
    frontImage = models.CharField(max_length=255)
    textTitle = models.CharField(max_length=255)
    contentNote = models.TextField()
    date = models.DateField(auto_now_add=True, null=True)
    categoryBlog = models.CharField(max_length=255)
    createdBy = models.ForeignKey(UsersM, on_delete=models.CASCADE)
    nameCreator =  models.CharField(max_length=255)