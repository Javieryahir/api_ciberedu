from django.db import models
from user.models import UsersM


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    createdBy = models.ForeignKey(UsersM, on_delete=models.CASCADE)
    nameCreator =  models.CharField(max_length=255)
    creationDate = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    content = models.TextField()
    categoryId = models.ForeignKey(Category, related_name='messageCa',on_delete=models.CASCADE)
    createdBy = models.ForeignKey(UsersM, on_delete=models.CASCADE)
    nameCreator =  models.CharField(max_length=255)
    creationDate = models.DateTimeField(auto_now_add=True)

