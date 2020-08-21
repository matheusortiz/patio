from django.urls import path
from . import views

app_name = 'remocoes'

urlpatterns = [
    path('', views.inicial, name='home'),
    path('remocao/', views.remocao, name='remocao'),
    path('remocao/<int:id>/', views.remocao_detalhe, name='remocao_detalhe'),
    path('remocao/remocao_form/', views.remocao_form, name='remocao_form'),
    path('liberacao/', views.liberacao, name='liberacao'),
    path('patio/', views.patio, name='patio'),
    path('setor/', views.setor, name='setor'),
    path('suporte/', views.suporte, name='suporte'),
]