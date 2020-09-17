from django.shortcuts import render, get_object_or_404
from .models import Remocao, Patio, Setor, Liberacao
from .forms import Suporte, CadastroRemocaoForm, CadastroSetorForm, CadastroPatioForm, CadastroLiberacaoForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicial(request):
    return render(request, 'inicial.html')


@login_required
def setor(request):
    setores = Setor.objects.all()
    context = {
        'setores' : setores
    }
    return render(request, 'setor.html', context)


@login_required
def setor_cadastro(request):
    context = {}
    if request.method == 'POST':
        form = CadastroSetorForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form = CadastroSetorForm(request.POST)
            if form.save():
                context['success'] = True
                form = CadastroSetorForm()
    else:
        form = CadastroSetorForm()
    context['form'] = form
    return render(request, 'setor_form.html', context)


@login_required
def remocao(request):
    remocoes = Remocao.objects.all()
    context = {
        'remocoes' : remocoes
    }
    return render(request, 'remocao.html', context)

@login_required     
def remocao_detalhe(request, id):
    remocao = get_object_or_404(Remocao, id=id)
    context = {
        'remocao': remocao
        }
    return render(request, 'remocao_detalhe.html', context)

@login_required
def remocao_cadastro(request):
    context = {}
    if request.method == 'POST':
        form = CadastroRemocaoForm(request.POST, request.FILES, request.user)
        if form.is_valid():
            context['success'] = True
            form.save()
            form = CadastroRemocaoForm()
    else:
        form = CadastroRemocaoForm()
    context['form'] = form
    return render(request, 'remocao_form.html', context)


@login_required
def liberacao(request):
    liberacoes = Liberacao.objects.all()
    context = {
        'liberacoes' : liberacoes
    }
    return render(request, 'liberacao.html', context)

@login_required     
def liberacao_detalhe(request, id):
    liberacao = get_object_or_404(Liberacao, id=id)
    context = {
        'liberacao': liberacao
        }
    return render(request, 'liberacao_detalhe.html', context)

@login_required
def liberacao_cadastro(request):
    context = {}
    if request.method == 'POST':
        form = CadastroLiberacaoForm(request.POST, request.FILES)
        if form.is_valid():
            context['success'] = True
            form.save()
            form = CadastroLiberacaoForm()
    else:
        form = CadastroLiberacaoForm()
    context['form'] = form
    return render(request, 'liberacao_form.html', context)


@login_required
def patio(request):
    patios = Patio.objects.all()
    context = {
        'patios' : patios
    }
    return render(request, 'patio.html', context)


@login_required
def patio_cadastro(request):
    context = {}
    if request.method == 'POST':
        form = CadastroPatioForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form = CadastroPatioForm(request.POST)
            if form.save():
                context['success'] = True
                form = CadastroPatioForm()
    else:
        form = CadastroPatioForm()
    context['form'] = form
    return render(request, 'patio_form.html', context)


@login_required
def suporte(request):
    context = {}
    if request.method == 'POST':
        form = Suporte(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail()
            form = Suporte()
    else:
        form = Suporte()
    context['form'] = form
    return render(request, 'suporte.html', context)
