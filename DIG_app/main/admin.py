from django.contrib import admin
from .models import Establecimiento, Usuario

# Register your models here.
# class UsuarioAdmin(admin.ModelAdmin):
#     fields = [
#         "nombre"
    
#     ]

admin.site.register(Usuario)
admin.site.register(Establecimiento)