from django.contrib.auth.models import User
from django.db import models

from apps.empresas.models import Empresa
from phonenumber_field.modelfields import PhoneNumberField


class Cliente(models.Model):
    empresa = models.ForeignKey(Empresa, default=1, on_delete=models.PROTECT)
    user = models.OneToOneField(User, default=1, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100, help_text="Nome do Cliente")
    telefone_celular = PhoneNumberField(blank=True)

    class Meta:
        unique_together = ('empresa', 'nome')
        ordering = ['nome']

    def __str__(self):
        return self.nome
