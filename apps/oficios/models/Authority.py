from oficios.models import *
from datetime import datetime

class Authority(models.Model):
    #TODO: incluir campo para cargo
    name = models.CharField(null=False, max_length=200)
    institution = models.CharField(max_length=200)
    state = models.ForeignKey(State, null=True, related_name='state', on_delete=models.SET_NULL)
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
        return '{}'.format(self.name, self.institution)
