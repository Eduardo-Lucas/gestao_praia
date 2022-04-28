from django.db import models

from apps.empresas.models import Empresa
from apps.funcionarios.models import Funcionario
from apps.produtos.models import Produto


class Mesa(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    numero = models.CharField(max_length=3, help_text='Número da Mesa')
    disponivel = models.BooleanField(default=True, help_text='Indica se a mesa está disponível para novos pedidos')

    class Meta:
        unique_together = ('empresa', 'numero')
        ordering = ['funcionario', 'numero']

    def __str__(self):
        return self.numero


class Pedido(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT, help_text='Funcionário que atende a mesa')
    mesa = models.ForeignKey(Mesa, on_delete=models.PROTECT, help_text='Número da mesa sendo atendida')
    aberto = models.BooleanField(default=True, help_text='Indica se a comanda está aberta ou fechada')
    fechado_as = models.DateTimeField(auto_now=True)


class PedidoItens(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, help_text='Produto sendo pedido')
    solicitado_as = models.DateTimeField(auto_created=True, help_text='Hora que foi feito o pedido na comando')


