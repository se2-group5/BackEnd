from pyexpat import model
from django.db import models
import datetime

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    puntaje = models.DecimalField(max_digits=2, decimal_places=1)
    correo = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'id: {self.id} {self.nombre}'


class Establecimiento(models.Model):
    nombre = models.CharField(max_length=100) 
    horario_apertura = models.TimeField(default=datetime.time(8, 0, 0), name='Apertura')
    horario_cierre = models.TimeField(default=datetime.time(19, 0, 0) , name='Cierre')
    ciudad = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    calidad_internet = models.DecimalField(max_digits=2, decimal_places=1)
    calificacion = models.DecimalField(max_digits=2, decimal_places=1)
    descripcion = models.TextField()

    def __str__(self) -> str:
        return f'{self.id} {self.nombre} {self.tipo}'

# date_published = models.DateTime

    
