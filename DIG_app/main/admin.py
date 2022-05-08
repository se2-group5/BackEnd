from django.contrib import admin
from .models import Business, User
#from django.db import models

#Register your models here.
# class EstablecimientoAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ( "Nombre y Ciudad", {"fields" : ["nombre", "ciudad"]}  ),
#         ( "Horario", {"fields": ["Apertura", "Cierre"]} ),
#     ]


admin.site.register(User)
admin.site.register(Business)
#admin.site.register(Establecimiento, EstablecimientoAdmin)