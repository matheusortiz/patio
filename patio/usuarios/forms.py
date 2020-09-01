from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from patio.utils import generate_hash_key
from remocoes.forms import send_mail
from .models import PasswordReset

User = get_user_model()

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='Email')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError('Email inválido.')

    def salvar(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        chave = generate_hash_key(user.username)
        reset = PasswordReset(chave=chave, user=user)
        reset.save()
        msg = 'Para recuperar a senha acesso o link: http://127.0.0.1:8000/contas/senha_reset_email/' + reset.chave
        assunto = 'Criar nova senha no AppPátio'
        contexto = {
            'reset': reset,
        }
        send_mail(assunto, msg, contexto, [user.email])


class RegistrarUsuarioForm(forms.ModelForm):

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de senha', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Confirmação incorreta', code='password_mismatch',)
        return password2

    def save(self, commit=True):
        user = super(RegistrarUsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'graduacao', 'opm']

class EditarUsuarioForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'graduacao', 'opm']