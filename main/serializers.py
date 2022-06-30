from rest_framework import serializers
from .models import *

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super(BusinessSerializer, self).to_representation(instance)
        rep['city'] = instance.city.name
        return rep

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class ConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consult
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super(ReportSerializer, self).to_representation(instance)
        rep['user_id'] = instance.user_id.username
        rep['occupation_status'] = instance.occupation_status.status
        return rep

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        #fields = ['id', 'username', 'email', 'is_active', 'created', 'updated']
        #read_only_field = ['is_active', 'created', 'updated']

    def to_representation(self, instance):
        rep = super(UserSerializer, self).to_representation(instance)
        rep['city'] = instance.city.name
        return rep