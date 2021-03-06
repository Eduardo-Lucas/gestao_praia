# Generated by Django 3.2.13 on 2022-04-28 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0005_auto_20220428_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidoitem',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='pedidos.pedido'),
        ),
        migrations.AlterField(
            model_name='pedidoitem',
            name='quantidade',
            field=models.PositiveIntegerField(default=1, help_text='Quantidade pedida'),
        ),
    ]
