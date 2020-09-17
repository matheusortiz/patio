from django.urls import path
from . import views

app_name = 'remocoes'

urlpatterns = [
    path('', views.inicial, name='home'),
    path('remocao/', views.remocao, name='remocao'),
    path('remocao/<int:id>/', views.remocao_detalhe, name='remocao_detalhe'),
    path('remocao/cadastro/', views.remocao_cadastro, name='remocao_cadastro'),
    path('liberacao/', views.liberacao, name='liberacao'),
    path('liberacao/<int:id>/', views.liberacao_detalhe, name='liberacao_detalhe'),
    path('liberacao/cadastro/', views.liberacao_cadastro, name='liberacao_cadastro'),
    path('patio/', views.patio, name='patio'),
    path('patio/cadastro', views.patio_cadastro, name='patio_cadastro'),
    path('setor/', views.setor, name='setor'),
    path('setor/<int:id>/', views.setor, name='setor'),
    path('setor/cadastro/', views.setor_cadastro, name='setor_cadastro'),
    path('suporte/', views.suporte, name='suporte'),
]
    