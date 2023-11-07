from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import noteBook, notesPages

admin.site.register(noteBook)
admin.site.register(notesPages)