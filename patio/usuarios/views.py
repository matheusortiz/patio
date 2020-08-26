from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.conf import settings
from .forms import RegistrarUsuarioForm, EditarUsuarioForm
from django.contrib.auth.decorators import login_required

def cadastrar(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = RegistrarUsuarioForm()
    contexto = {
        'form': form
    }
    return render(request, 'cadastro.html', contexto)


@login_required
def painel(request):
    return render(request, 'painel.html')


@login_required
def editar(request):
    contexto = {}
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditarUsuarioForm(instance=request.user)
            contexto['success'] = True
    else:
        form = EditarUsuarioForm(instance=request.user)
    contexto['form'] = form
    return render(request, 'usuario_edit.html', contexto)


@login_required
def editar_senha(request):
    contexto = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            contexto['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    contexto['form'] = form
    return render(request, 'senha_edit.html', contexto)