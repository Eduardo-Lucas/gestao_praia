from django.contrib.auth.models import User
from django.db import models

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    empresa = models.ForeignKey(Empresa, default=1, on_delete=models.PROTECT)
    user = models.OneToOneField(User, default=1, on_delete=models.PROTECT)
    departamento = models.ForeignKey(Departamento, default=1, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100, help_text="Nome do Funcionário")

    class Meta:
        unique_together = ('empresa', 'nome')

    def __str__(self):
        return self.nome
