from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .forms import RegistrarUsuarioForm, EditarUsuarioForm
from django.contrib.auth.decorators import login_required

def cadastro(request):
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
def editar_usuario(request):
    form = EditarUsuarioForm()
    contexto = {
        'form' : form
    }
    return render(request, 'usuario_edit.html', contexto)