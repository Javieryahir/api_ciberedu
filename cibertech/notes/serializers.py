from .models import noteBook
from rest_framework import serializers




class noteBookSerializers(serializers.ModelSerializer):

    class Meta:
        model = noteBook
        fields = '__all__'
        read_only_fields = ['createdBy', 'nameCreator']

class noteBookSerializersCreate(serializers.ModelSerializer):

    class Meta:
        model = noteBook
        fields = '__all__'
        read_only_fields = ['createdBy', 'nameCreator']

