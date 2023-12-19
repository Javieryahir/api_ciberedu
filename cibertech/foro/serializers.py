from .models import Category, Message
from rest_framework import serializers




class categorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['createdBy', 'nameCreator']

class messageSerializers(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['createdBy', 'nameCreator']


class categoryMessageSerializers(serializers.ModelSerializer):

    messageCa = messageSerializers(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ['messageCa']