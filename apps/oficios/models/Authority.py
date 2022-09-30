from email.policy import default
from random import choices
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
    name = models.CharField(null=False, max_length=200)
    post = models.CharField(null=True, blank=True, max_length=200, default=None)
    institution = models.CharField(max_length=200)
    state = models.CharField(null=False, max_length=2, choices=STATE_CHOICES, default='SP')
    city = models.CharField(null=True, blank=True, max_length=200)
    address = models.CharField(null=True, blank=True, max_length=200)
    number = models.CharField(null=True, blank=True, max_length=10)
    complement = models.CharField(null=True, blank=True, max_length=200)
    cep = models.CharField(null=True, blank=True, max_length=8)
    email = models.EmailField(null=True, blank=True, max_length=100)
    phone = models.CharField(null=True, blank=True, max_length=50) 
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Autoridade'
        verbose_name_plural = 'Autoridades'
    def __str__(self):
        return '{}'.format(self.name, self.post, self.institution)
