from django.shortcuts import render, get_object_or_404
from .models import Remocao
from .forms import CadastroRemocao, Suporte

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

def remocao_form(request):
    contexto = {}
    if request.method == 'POST':
        form = CadastroRemocao(request.POST)
        if form.is_valid():
            contexto['is_valid'] = True
            form = CadastroRemocao()
    else:
        form = CadastroRemocao()

    contexto['form'] = form

    return render(request, 'remocao_form.html', contexto)


def liberacao(request):
    return render(request, 'liberacao.html')

def patio(request):
    return render(request, 'patio.html')

def setor(request):
    return render(request, 'setor.html')

def suporte(request):
    contexto = {}
    if request.method == 'POST':
        form = Suporte(request.POST)
        if form.is_valid():
            contexto['is_valid'] = True
            form.send_mail()
            form = Suporte()
    else:
        form = Suporte()

    contexto['form'] = form

    return render(request, 'suporte.html', contexto)