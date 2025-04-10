# Generated by Django 5.1.3 on 2025-01-18 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrecoServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo: ')),
                ('icone', models.CharField(choices=[('lni-package', 'Caixa'), ('lni-drop', 'Drop'), ('lni-star', 'Estrela')], max_length=12, verbose_name='Icone')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('usuarios', models.CharField(max_length=100, verbose_name='Usuários')),
                ('gbStorage', models.CharField(max_length=100, verbose_name='Armazenamento')),
                ('tipeEmailSuport', models.CharField(max_length=25, verbose_name='Estatus de Email Suporte')),
                ('lifetimeUpdates', models.BooleanField(default=True, verbose_name='LifetimesUpdates')),
            ],
            options={
                'verbose_name': 'PreçoServiço',
                'verbose_name_plural': 'PreçoServiços',
            },
        ),
    ]
