from email.policy import default
from random import choices
from tabnanny import verbose
from oficios.models import *
from datetime import datetime

STATE_CHOICES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceara'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'), 
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE',	'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC',	'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE',	'Sergipe'),
    ('TO', 'Tocantins'),
)

class Authority(models.Model):
    name = models.CharField(null=False, max_length=200, verbose_name='Nome')
    post = models.CharField(null=True, blank=True, max_length=200, default=None, verbose_name='Cargo/Função')
    institution = models.CharField(max_length=200, verbose_name='Órgão/Instituição')
    state = models.CharField(null=False, max_length=2, choices=STATE_CHOICES, default='SP', verbose_name='Estado')
    city = models.CharField(null=True, blank=True, max_length=200, verbose_name='Cidade')
    address = models.CharField(null=True, blank=True, max_length=200, verbose_name='Endereço')
    number = models.CharField(null=True, blank=True, max_length=10, verbose_name='Número')
    complement = models.CharField(null=True, blank=True, max_length=200, verbose_name='Complemento')
    cep = models.CharField(null=True, blank=True, max_length=8, verbose_name='CEP')
    email = models.EmailField(null=True, blank=True, max_length=100)
    phone = models.CharField(null=True, blank=True, max_length=50, verbose_name='Telefone') 
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Autoridade'
        verbose_name_plural = 'Autoridades'
    def __str__(self):
        return '{}'.format(self.institution)
