from django.db import models

class Etilometro(models.Model):

    marca = models.CharField('Marca', max_length=300, blank=True)
    modelo = models.CharField('Modelo', max_length=300, blank=True)
    numero_serie = models.IntegerField('Numero de série')
    validade = models.DateField('Data de validade')
    local = models.CharField('Local', max_length=300, blank=True)
    certificado = models.FileField(upload_to='cert_etil', verbose_name='Certificado de etilômetro', null=True, blank=True)
    observacoes = models.TextField('Observações', blank=True, null=True)
    ativo = models.BooleanField('Ativo', default=0)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True, null=True)


    def __str__(self):
        return str(self.numero_serie)

    class Meta:
        verbose_name = 'Etilômetro'
        verbose_name_plural = 'Etilômetros'
        ordering = ['ativo', 'numero_serie']
