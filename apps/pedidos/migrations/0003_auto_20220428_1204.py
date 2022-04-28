# Generated by Django 3.2.13 on 2022-04-28 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_rename_pedidoitens_pedidoitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mesa',
            options={'ordering': ['disponivel', 'numero']},
        ),
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ['-aberto', 'funcionario', 'mesa', 'aberto']},
        ),
        migrations.RemoveField(
            model_name='mesa',
            name='cliente',
        ),
    ]
