import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core import validators

class Usuario(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Usuário', max_length=50, unique=True, validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'),
            'Nome de usuário inválido.',
            'invalid' )]
        )
    email = models.EmailField('Email Institucional', unique=True)
    name = models.CharField('Nome', max_length=100)
    graduacao = models.CharField('Graduação', max_length=100)
    opm = models.CharField('OPM', max_length=100)
    is_active = models.BooleanField('Ativo?', blank=True, default=False)
    is_staff = models.BooleanField('Administrador?', blank=True, default=False)
    data_cadastro = models.DateTimeField('Data de cadastro', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
