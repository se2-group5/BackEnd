from django.contrib import admin
from .models import Business, Consult, User, Report, Favorite, OccupationStatus, City
#from django.db import models

#Register your models here.
# class EstablecimientoAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ( "Nombre y Ciudad", {"fields" : ["nombre", "ciudad"]}  ),
#         ( "Horario", {"fields": ["Apertura", "Cierre"]} ),
#     ]

# class ConsultAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ( "Date", {"fields" : ["date"]}  ),
#         ( "Who consulted and which business", {"fields": ["user_id", "business_id"]} )
#     ]

admin.site.register(User)
admin.site.register(Business)
admin.site.register(Consult)
admin.site.register(Report)
admin.site.register(Favorite)
admin.site.register(OccupationStatus)
admin.site.register(City)
#admin.site.register(Establecimiento, EstablecimientoAdmin)