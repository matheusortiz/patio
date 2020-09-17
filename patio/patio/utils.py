import hashlib
import string
import random

# geração de chave para recuperação de senha
def random_key(size=5):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))


def generate_hash_key(salt, random_str_size=5):
    random_str = random_key(random_str_size)
    text = random_str + salt
    return hashlib.sha224(text.encode('utf-8')).hexdigest()

# constantes
UF = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espirito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
)

ESPECIES = (
    ('Passageiro', 'Passageiro'),
    ('Carga', 'Carga'),
    ('Misto', 'Misto'),
    ('Competição', 'Competição'),
    ('Tração', 'Tração'),
    ('Especial', 'Especial'),
    ('Coleção', 'Coleção')
)

TIPOS = (
    ('Automóvel',  'Automóvel'),
    ('Camioneta',  'Camioneta'),
    ('Caminhão',  'Caminhão'),
    ('Reboque',  'Reboque'),
    ('Ônibus',  'Ônibus'),
    ('Micro',  'Micro-ônibus'),
    ('Trator',  'Trator'),
    ('Guincho',  'Guincho'),
    ('Motocicleta',  'Motocicleta'),
    ('Motoneta',  'Motoneta'),
    ('Ciclomotor', 'Ciclomotor'),
    ('Triciclo', 'Triciclo'),
    ('Bicicleta', 'Bicicleta'),
    ('Prototipo', 'Prototipo')
)

COMBUSTIVEIS = (
    ('G', 'Gasolina'),
    ('E', 'Etanol'),
    ('F', 'Flex'),
    ('D', 'Diesel'),
    ('Ele', 'Elétrico'),
    ('PH', 'Propulsão humana'),
    ('T', 'Tração'),
)

CORES = (
    ('Amarela', 'Amarela'),
    ('Azul', 'Azul'),
    ('Bege', 'Bege'),
    ('Branca', 'Branca'),
    ('Cinza', 'Cinza'),
    ('Dourada', 'Dourada'),
    ('Laranja', 'Laranja'),
    ('Marrom', 'Marrom'),
    ('Prata', 'Prata'),
    ('Preta', 'Preta'),
    ( 'Roxa', 'Roxa'),
    ( 'Verde', 'Verde'),
    ( 'Vermelha', 'Vermelha'),
    ( 'Incendiado', 'Incendiado')
)
