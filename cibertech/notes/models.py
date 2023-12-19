from django.db import models
from user.models import UsersM



class noteBook(models.Model):
    bookTitle = models.CharField(max_length=100)
    bookLink = models.TextField()
    image = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True, null=True)
    createdBy = models.ForeignKey(UsersM, on_delete=models.CASCADE)
    nameCreator =  models.CharField(max_length=255)


