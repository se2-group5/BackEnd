from django.contrib import admin
from .models import Establecimiento, Usuario
from django.db import models

#Register your models here.
# class EstablecimientoAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ( "Nombre y Ciudad", {"fields" : ["nombre", "ciudad"]}  ),
#         ( "Horario", {"fields": ["Apertura", "Cierre"]} ),
#     ]


admin.site.register(Usuario)
admin.site.register(Establecimiento)
#admin.site.register(Establecimiento, EstablecimientoAdmin)