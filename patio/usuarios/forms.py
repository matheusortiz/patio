from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrarUsuarioForm(UserCreationForm):

    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email já cadastrado.')
        return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class EditarUsuarioForm(forms.ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Email já cadastrado.')
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']