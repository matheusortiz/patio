from django.db import models
from datetime import datetime
from patio import settings, utils

class Patio(models.Model):
    descricao = models.CharField('Descrição', max_length=300)
    observacoes = models.TextField('Observações', blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Pátio'
        verbose_name_plural = 'Pátios'
        ordering = ['descricao']

class Setor(models.Model):
    descricao = models.CharField('Descrição', max_length=300)
    coluna = models.CharField('Coluna', max_length=300, null=True, blank=True)
    fileira = models.CharField('Fileira', max_length=300, null=True, blank=True)
    patio = models.ForeignKey(Patio, on_delete=models.SET_NULL, null=True, blank=True)
    observacoes = models.TextField('Observações', blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'
        ordering = ['descricao']


class Liberacao(models.Model):
    numero_processo = models.CharField('Processo', max_length=50, blank=True)
    data_liberacao = models.DateField('Data de Liberação')
    documento_liberacao = models.FileField(
        upload_to='doc_liberacao', verbose_name='Documento de Liberação')
    observacoes = models.TextField('Observações', blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Liberação'
        verbose_name_plural = 'Liberações'
        ordering = ['data_liberacao']

    def __str__(self):
        if self.observacoes == '':
            return self.numero_processo + ' - ' + str(self.data_liberacao.strftime('%d/%m/%Y'))
        else:
            return self.numero_processo + ' - ' + str(self.data_liberacao.strftime('%d/%m/%Y')) + ' - ' + self.observacoes

class Remocao(models.Model):

    plaqueta = models.IntegerField('Plaqueta')
    placa = models.CharField('Placa', max_length=7, blank=True)
    uf = models.CharField('UF', choices=utils.UF, max_length=2 , default='PR', blank=True)
    data_vistoria = models.DateField('Data de Vistoria')
    patio = models.ForeignKey(Patio, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    marca = models.CharField('Marca', max_length=300, blank=True)
    modelo = models.CharField('Modelo', max_length=300, blank=True)
    especie = models.CharField('Especie', choices=utils.ESPECIES ,  default='Passageiro', max_length=300)
    tipo = models.CharField('Tipo', choices=utils.TIPOS, default='Automóvel', max_length=300)
    combustivel = models.CharField('Combustível', choices=utils.COMBUSTIVEIS, default='G', max_length=300, blank=True, null=True)
    cor = models.CharField('Cor', choices=utils.CORES, max_length=300)
    chassi = models.CharField('Chassi', max_length=300, blank=True)
    observacoes = models.TextField('Observações', blank=True, null=True)
    documento_remocao = models.FileField(upload_to='doc_remocao', verbose_name='Documento de Remoção')
    bloqueio_judicial = models.BooleanField('BJ', blank=True)
    liberacao = models.ForeignKey(Liberacao, on_delete=models.SET_NULL, null=True, blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True, null=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='remocoes', on_delete=models.CASCADE)

    def __str__(self):
        return self.placa
    
    class Meta:
        verbose_name = 'Remoção'
        verbose_name_plural = 'Remoções'
