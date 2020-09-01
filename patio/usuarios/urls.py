from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('senha_reset/', views.password_reset, name='reset'),
    path('senha_reset_email/<chave>/', views.password_reset_confirm, name='reset_email'),
    path('painel/', views.painel, name='painel'),
    path('editar/', views.editar, name='editar'),
    path('senha/', views.editar_senha, name='senha'),
]
