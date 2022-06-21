from django.db import models
from django.contrib.auth.models import AbstractUser


#USEFUL COMMANDS
#  python manage.py showmigrations
# python3 manage.py makemigrations <nameofapp>

import datetime

# Create your models here.
# class Usuario(models.Model):
#     nombre = models.CharField(max_length=55)
#     puntaje = models.DecimalField(max_digits=2, decimal_places=1)
#     correo = models.CharField(max_length=100)
#     ciudad = models.CharField(max_length=30)
#     telefono = models.CharField(max_length=20)

#     def __str__(self) -> str:
#         return f'id: {self.id} {self.nombre}'

# Custom User Class

class OccupationStatus(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.status}'

class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.name}'

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254,unique=True, null=True, blank=True)
    avatar = models.ImageField(upload_to='main/images/user_profile', blank=True) # Uses Pillow Lib, see requirements.
    
    # more specific to business logic
    city = models.ForeignKey(City, default=1, verbose_name='City', on_delete=models.SET_DEFAULT)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    telephone_number = models.CharField(max_length=15, null=True, blank=True)


    def __str__(self) -> str:
         return f'id: {self.id} {self.first_name} {self.email}'

    class Meta(AbstractUser.Meta):
       swappable = 'AUTH_USER_MODEL'


class Business(models.Model):
    name = models.CharField(max_length=100) 
    opening_time = models.TimeField(default=datetime.time(8, 0, 0), name='Opening')
    closing_time = models.TimeField(default=datetime.time(19, 0, 0) , name='Closing')
    city = models.ForeignKey(City, default=1, verbose_name='City', on_delete=models.SET_DEFAULT)
    type = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    capacity = models.IntegerField()
    internet_quality = models.DecimalField(max_digits=2, decimal_places=1)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    description = models.TextField()
    telephone_number = models.CharField(max_length=15, null=True, blank=True)
    cover_picture = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.type}'


class Consult(models.Model):
    date = models.DateTimeField(auto_now_add=True, auto_now=False) # Automatically add now as DateTime when created, but not when modified.
    user_id = models.ForeignKey(User, default=1, verbose_name='UserID', on_delete=models.SET_DEFAULT)
    business_id = models.ForeignKey(Business, default=1, verbose_name='BusinessID', on_delete=models.SET_DEFAULT)

    def __str__(self) -> str:
         return f'{self.user_id} {self.date}'    


class Report(models.Model):
    date = models.DateTimeField(auto_now_add=True, auto_now=False) # Automatically add now as DateTime when created, but not when modified.
    user_id = models.ForeignKey(User, default=1, verbose_name='UserID', on_delete=models.SET_DEFAULT)
    business_id = models.ForeignKey(Business, default=1, verbose_name='BusinessID', on_delete=models.SET_DEFAULT)
    occupation_status = models.ForeignKey(OccupationStatus, default=1, verbose_name='Ocupation', on_delete=models.SET_DEFAULT)
    internet_status = models.DecimalField(max_digits=2, decimal_places=1) # make a difference from internet_quality
    rating_business = models.DecimalField(max_digits=2, decimal_places=1) # Should go from 1 to 5
    report_support = models.IntegerField(null=True, default=0)
    comments = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
         return f'Report made by {self.user_id} on {self.date}'

class Favorite(models.Model):
    user_id = models.ForeignKey(User, default=1, verbose_name='UserID', on_delete=models.SET_DEFAULT)
    business_id = models.ForeignKey(Business, default=1, verbose_name='BusinessID', on_delete=models.SET_DEFAULT)

    def __str__(self) -> str:
         return f'{self.user_id} tiene por favorito a {self.business_id}'
    
    
