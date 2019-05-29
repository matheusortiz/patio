from django.db import models

# Create your models here.


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


class Liberacao(models.Model):
    data_liberacao = models.DateField('Data de Liberação')
    documento_liberacao = models.ImageField(
        upload_to='doc_liberacao', verbose_name='Documento de Liberação')
    observacoes = models.TextField('Observações', blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.observacoes

        class Meta:
            verbose_name = 'Liberação'
            verbose_name_plural = 'Liberações'


class Remocao(models.Model):
    plaqueta = models.IntegerField('Plaqueta')
    placa = models.CharField('Placa', max_length=7)
    uf = models.CharField('UF', max_length=2)
    data_vistoria = models.DateField('Data de Vistoria')
    patio = models.ForeignKey(Patio, on_delete=models.CASCADE)
    marca = models.CharField('Marca', max_length=300)
    modelo = models.CharField('Modelo', max_length=300)
    especie = models.CharField('Especie', max_length=300, blank=True)
    tipo = models.CharField('Tipo', max_length=300, blank=True)
    combustivel = models.CharField('Combustível', max_length=300, blank=True)
    cor = models.CharField('Cor', max_length=300, blank=True)
    chassi = models.CharField('Chassi', max_length=300, blank=True)
    observacoes = models.TextField('Observações', blank=True)
    documento_remocao = models.ImageField(
        upload_to='doc_remocao', verbose_name='Documento de Remoção')
    bloqueio_judicial = models.BooleanField('BJ', blank=True)
    liberacao = models.ForeignKey(
        Liberacao, on_delete=models.CASCADE, null=True, blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.placa

    class Meta:
        verbose_name = 'Remoção'
        verbose_name_plural = 'Remoções'
