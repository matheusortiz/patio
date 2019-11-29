from django.contrib import admin

# Register your models here.

from .models import Etilometro

class EtilometroAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'numero_serie', 'validade', 'local']
    search_fields = ['numero_serie']

admin.site.register(Etilometro, EtilometroAdmin)