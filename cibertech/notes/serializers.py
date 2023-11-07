from .models import noteBook, notesPages
from rest_framework import serializers




class noteBookSerializers(serializers.ModelSerializer):

    class Meta:
        model = noteBook
        fields = '__all__'

class notePagesSerializers(serializers.ModelSerializer):

    class Meta:
        model = notesPages
        fields = '__all__'


class notePagesBookSerializers(serializers.ModelSerializer):
    notesPagesB = notePagesSerializers(many=True,read_only=True)
    class Meta:
        model = noteBook
        fields = ['notesPagesB']