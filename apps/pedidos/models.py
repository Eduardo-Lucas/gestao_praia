from django.db import models

from apps.clientes.models import Cliente
from apps.empresas.models import Empresa
from apps.funcionarios.models import Funcionario
from apps.produtos.models import Produto


class Mesa(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    numero = models.CharField(max_length=10, default='Avulso 01', help_text='Número da Mesa')
    disponivel = models.BooleanField(default=True, help_text='Indica se a mesa está disponível para novos pedidos')

    class Meta:
        unique_together = ('empresa', 'numero')
        ordering = ['disponivel', 'numero']

    def __str__(self):
        return f'Mesa {self.numero}'


class Pedido(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT, help_text='Funcionário que atende a mesa')
    mesa = models.ForeignKey(Mesa, on_delete=models.PROTECT, help_text='Número da mesa sendo atendida')
    aberto = models.BooleanField(default=True, help_text='Indica se a comanda está aberta ou fechada')
    fechado_as = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-aberto', 'funcionario', 'mesa', 'aberto']

    def total_items(self):
        return str(
            sum(
                pedidoitem.total_preco_bruto() for pedidoitem in self.items.all()
            )
                   )

    def taxa_de_servico(self):
        return str(
            float(self.total_items()) * float(0.10)

        )

    def total_pedido(self):
        return str(
            float(self.total_items()) + float(self.taxa_de_servico())
        )

    def __str__(self):
        return f'Pedido: {str(self.id)} - Total dos Itens: {self.total_items()} + ' \
               f'Taxa de Serviço: {self.taxa_de_servico()} - Total do Pedido: {self.total_pedido()}'


class PedidoItem(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    pedido = models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, help_text='Produto sendo pedido')
    quantidade = models.PositiveIntegerField(default=1, help_text='Quantidade pedida')
    solicitado_as = models.DateTimeField(auto_created=True, help_text='Hora que foi feito o pedido na comando')

    class Meta:
        ordering = ['solicitado_as']

    def __str__(self):
        return f'Pedido: {self.pedido} - Sequência: {str(self.id)} - Produto: {self.produto} - ' \
               f'Preço: {str(self.produto.preco)} x {self.quantidade}'

    def total_preco_bruto(self):
        return self.produto.preco * self.quantidade
