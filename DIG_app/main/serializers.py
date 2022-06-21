from rest_framework import serializers
from .models import Business, User

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('id', 'name', 'city', 'capacity', 'description')

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'title', 'description', 'completed')