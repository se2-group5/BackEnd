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
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254,unique=True, null=True, blank=True)
    avatar = models.ImageField(upload_to='thumbpath', blank=True) # Uses Pillow Lib, see requirements.
    
    # more specific to business logic
    city = models.CharField(max_length=30, null=True)
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
    city = models.CharField(max_length=30)
    type = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    capacity = models.IntegerField()
    internet_quality = models.DecimalField(max_digits=2, decimal_places=1)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    description = models.TextField()
    telephone_number = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.type}'




    
