from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.conf import settings
from .forms import RegistrarUsuarioForm, EditarUsuarioForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import PasswordReset
from patio.utils import generate_hash_key

Usuario = get_user_model()

def cadastrar(request):
    contexto = {}
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            contexto['success'] = True
    else:
        form = RegistrarUsuarioForm()
    contexto['form'] = form
    return render(request, 'cadastro.html', contexto)

def password_reset(request):
    contexto = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.salvar()
        contexto['success'] = True
    contexto['form'] = form
    return render(request, 'senha_reset.html', contexto)

def password_reset_confirm(request, chave):
    contexto = {}
    reset = get_object_or_404(PasswordReset, chave=chave)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        contexto['success'] = True
    contexto['form'] = form
    return render(request, 'senha_reset_email.html', contexto)

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