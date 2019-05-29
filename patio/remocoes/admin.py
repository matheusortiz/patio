from django.contrib import admin

# Register your models here.

from .models import Patio, Liberacao, Remocao

class RemocaoAdmin(admin.ModelAdmin):
    list_display = ['plaqueta', 'placa', 'uf', 'data_vistoria', 'patio']
    search_fields = ['plaqueta', 'placa']

admin.site.register(Patio)
admin.site.register(Liberacao)
admin.site.register(Remocao, RemocaoAdmin)