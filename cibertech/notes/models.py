from django.db import models
from ckeditor.fields import richTextField



class noteBook(models.Model):
    bookTitle = models.CharField(max_length=100)
    bookDescription = models.TextField()
    image = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True, null=True)
    

class notesPages(models.Model):
    contentNote = models.TextField()
    date = models.DateField(auto_now_add=True, null=True)
    noteBookId = models.ForeignKey(noteBook,related_name='notesPagesB',on_delete=models.RESTRICT)
