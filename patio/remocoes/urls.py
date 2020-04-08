from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('inicial/', views.inicial, name='inicial'),
    path('remocao/', views.remocao, name='remocao'),
    path('remocao/<int:id>/', views.remocao_detalhe, name='remocao_detalhe'),
    path('liberacao/', views.remocao, name='liberacao'),
    path('patio/', views.remocao, name='patio'),
    path('setor/', views.remocao, name='setor'),
]