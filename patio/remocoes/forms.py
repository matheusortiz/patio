from django import forms
from .models import Patio, Liberacao, Remocao, Setor
from django.core.mail import send_mail
from django.conf import settings
from patio import utils, settings
from django.forms import ModelForm

class Suporte(forms.Form):

    nome = forms.CharField(label='Nome', max_length=200)
    email = forms.EmailField(label='Email')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_mail(self):
        assunto = 'App Patio: Suporte de Sistema'
        mensagem = 'Nome: %(nome)s\n\nEmail: %(email)s\n\nMensagem: %(mensagem)s'
        contexto = {
             'nome': self.cleaned_data['nome'],
             'email': self.cleaned_data['email'],
             'mensagem': self.cleaned_data['mensagem'],
         }
        mensagem = mensagem % contexto
        send_mail(
            assunto, 
            mensagem, 
            settings.DEFAULT_FROM_EMAIL,
            settings.EMAIL_CONTATO
            )

class CadastroRemocaoForm(ModelForm):
    class Meta:
        model = Remocao
        fields = [
            'plaqueta', 'placa', 'uf', 'data_vistoria', 'patio', 
            'setor', 'marca', 'modelo', 'especie', 'tipo', 'combustivel',
            'cor', 'chassi', 'observacoes', 
            'documento_remocao', 'bloqueio_judicial', 'usuario'
            ]

class CadastroSetorForm(ModelForm):
    class Meta:
        model = Setor
        fields = [
            'descricao', 'coluna', 'fileira', 'patio', 'observacoes'
        ]


class CadastroPatioForm(ModelForm):
    class Meta:
        model = Patio
        fields = [
            'descricao', 'observacoes'
        ]


class CadastroLiberacaoForm(ModelForm):
    class Meta:
        model = Liberacao
        fields = [
            'numero_processo', 'data_liberacao', 'documento_liberacao', 'observacoes'
        ]