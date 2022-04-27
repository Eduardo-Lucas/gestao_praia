# Generated by Django 3.2.13 on 2022-04-27 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='departamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='departamentos.departamento'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]