from django import forms
from .models import Patio, Liberacao
from django.core.mail import send_mail
from django.conf import settings

class Suporte(forms.Form):

    nome = forms.CharField(label='Nome', max_length=200)
    email = forms.EmailField(label='Email')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_mail(self):
        assunto = 'App Patio: Suporte de Sistema'
        mensagem = 'Nome: %(nome)s;E-mail: %(email)s;%(mensagem)s'
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

class CadastroRemocao(forms.Form):

    patios = Patio.objects.all()

    PATIOS = ()
    for i in patios:
        PATIOS += (i.id, i.descricao),
    
    ESPECIES = (
        ('0', 'Passageiro'), 
        ('1', 'Carga'), 
        ('2', 'Misto'), 
        ('3', 'Competição'), 
        ('4', 'Tração'), 
        ('5', 'Especial'), 
        ('6', 'Coleção')
        )

    TIPOS = (
        ('0', 'Automóvel'), 
        ('1', 'Camioneta'), 
        ('2', 'Caminhão'), 
        ('3', 'Reboque'), 
        ('4', 'Ônibus'), 
        ('5', 'Micro-ônibus'), 
        ('6', 'Trator'),
        ('7', 'Guincho'), 
        ('8', 'Motocicleta'), 
        ('9', 'Motoneta'), 
        ('10', 'Ciclomotor'), 
        ('11', 'Triciclo'), 
        ('12', 'Bicicleta'), 
        ('13', 'Prototipo')
        )

    COMBUSTIVEIS = (
        ('0', 'Gasolina'), 
        ('1', 'Etanol'), 
        ('2', 'Diesel'), 
        ('4', 'Elétrico'), 
        ('5', 'Propulsão humana'), 
        ('6', 'Tração')  
        )

    CORES = (
        ('0', 'Amarela'), 
        ('1', 'Azul'), 
        ('2', 'Bege'), 
        ('3', 'Branca'), 
        ('4', 'Cinza'), 
        ('5', 'Dourada'), 
        ('6', 'Laranja'), 
        ('7', 'Marrom'), 
        ('8', 'Prata'), 
        ('9', 'Preta'), 
        ('10', 'Roxa'), 
        ('11', 'Verde'), 
        ('12', 'Vermelha'), 
        ('13', 'Incendiado')  
        )

    plaqueta = forms.IntegerField(label='Plaqueta')
    placa = forms.CharField(label='Placa', max_length=7)
    uf = forms.CharField(label='UF', max_length=2)
    data_vistoria = forms.DateField(label='Data de Vistoria')
    patio = forms.ChoiceField(label='Patio', choices=PATIOS)
    marca = forms.CharField(label='Marca', max_length=300)
    modelo = forms.CharField(label='Modelo', max_length=300)
    especie = forms.ChoiceField(label='Especie', choices=ESPECIES)
    tipo = forms.ChoiceField(label='Tipo', choices=TIPOS)
    combustivel = forms.MultipleChoiceField(label='Combustível', choices=COMBUSTIVEIS)
    cor = forms.ChoiceField(label='Cor', choices=CORES)
    chassi = forms.CharField(label='Chassi', max_length=300)
    observacoes = forms.CharField(label='Observações', widget=forms.Textarea, required=False)
    documento_remocao = forms.FileField(label='Documento de remoção', required=False)
    bloqueio_judicial = forms.BooleanField(label='Bloqueio Judicial', required=False)
    #liberacao = forms.ComboField(label='Liberação', fields=(cores))