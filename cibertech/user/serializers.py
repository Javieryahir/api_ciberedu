"""
Serializers for the user API View.
"""
from django.contrib.auth import ( get_user_model )
from django.utils.translation import gettext as _
from rest_framework import serializers

# serializers.py
from rest_framework import serializers
from .models import UsersM

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersM
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Establecer is_staff e is_superuser en False al crear el usuario
        validated_data['is_staff'] = False
        validated_data['is_superuser'] = False
        
        user = UsersM.objects.create_user(**validated_data)
        return user
    
   