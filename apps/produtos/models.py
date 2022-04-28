from django.db import models
from django.utils.text import slugify

from apps.empresas.models import Empresa


class Categoria(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    nome = models.CharField(max_length=50, help_text='Nome da Categoria')

    class Meta:
        unique_together = ('empresa', 'nome')
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Produto(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    nome = models.CharField(max_length=50, help_text='Nome do Produto')
    slug = models.SlugField(max_length=200, db_index=True, default=' ')
    image = models.ImageField(upload_to='produtos', blank=True, null=True)
    disponivel = models.BooleanField(default=True, help_text='Tem produto no estoque?')
    preco = models.DecimalField(max_digits=10, decimal_places=2, help_text='Preço do Produto')

    class Meta:
        unique_together = ('empresa', 'nome')
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def save(self):
        self.slug = slugify(self.descricao)
        super(Produto, self).save()
