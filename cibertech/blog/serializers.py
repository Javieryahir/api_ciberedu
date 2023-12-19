from .models import BlogPost
from rest_framework import serializers

class frontBlogSerializers(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ['frontImage', 'textTitle',]

class contentBlogSerializers(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = '__all__'
        read_only_fields = ['createdBy', 'nameCreator']