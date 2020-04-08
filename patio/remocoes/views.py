from django.shortcuts import render, get_object_or_404
from .models import Remocao

# Create your views here.

def login(request):
    return render(request, 'login.html')

def inicial(request):
    return render(request, 'inicial.html')

def remocao(request):
    remocoes = Remocao.objects.all()
    contexto = {
        'remocoes' : remocoes
    }
    return render(request, 'remocao.html', contexto)

def remocao_detalhe(request, id):
    remocao = get_object_or_404(Remocao, id=id)
    contexto = {
        'remocao': remocao
        }
    return render(request, 'remocao_detalhe.html', contexto)

def liberacao(request):
    return render(request, 'liberacao.html')

def patio(request):
    return render(request, 'patio.html')

def setor(request):
    return render(request, 'setor.html')