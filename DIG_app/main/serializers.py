from rest_framework import serializers
from .models import Business, User

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('id', 'name', 'city', 'capacity', 'description', 'cover_picture')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active', 'created', 'updated']
        read_only_field = ['is_active', 'created', 'updated']