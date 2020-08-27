from django.contrib import admin

from .models import Etilometro

class EtilometroAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'ativo', 'numero_serie', 'validade', 'local']
    search_fields = ['numero_serie']

admin.site.register(Etilometro, EtilometroAdmin)
