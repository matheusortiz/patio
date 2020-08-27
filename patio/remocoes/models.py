from django.db import models
from datetime import datetime

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
            return str(self.data_liberacao.strftime('%d/%m/%Y'))
        else:
            return str(self.data_liberacao.strftime('%d/%m/%Y')) + ' - ' + self.observacoes

class Remocao(models.Model):
    plaqueta = models.IntegerField('Plaqueta')
    placa = models.CharField('Placa', max_length=7, blank=True)
    uf = models.CharField('UF', max_length=2, blank=True)
    data_vistoria = models.DateField('Data de Vistoria')
    patio = models.ForeignKey(Patio, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    marca = models.CharField('Marca', max_length=300, blank=True)
    modelo = models.CharField('Modelo', max_length=300, blank=True)
    especie = models.CharField('Especie', max_length=300, blank=True, null=True)
    tipo = models.CharField('Tipo', max_length=300, blank=True, null=True)
    combustivel = models.CharField('Combustível', max_length=300, blank=True, null=True)
    cor = models.CharField('Cor', max_length=300, blank=True, null=True)
    chassi = models.CharField('Chassi', max_length=300, blank=True)
    observacoes = models.TextField('Observações', blank=True, null=True)
    documento_remocao = models.FileField(
        upload_to='doc_remocao', verbose_name='Documento de Remoção', null=True, blank=True)
    bloqueio_judicial = models.BooleanField('BJ', blank=True)
    liberacao = models.ForeignKey(Liberacao, on_delete=models.SET_NULL, null=True, blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True, null=True)

    def __str__(self):
        return self.placa

    
    class Meta:
        verbose_name = 'Remoção'
        verbose_name_plural = 'Remoções'
