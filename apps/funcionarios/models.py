from django.contrib.auth.models import User
from django.db import models

from apps.departamentos.models import Departamento


class Funcionario(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.PROTECT)
    departamento = models.ForeignKey(Departamento, default=1, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100, help_text="Nome do Funcionário")

    def __str__(self):
        return self.nome
