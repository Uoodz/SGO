# Generated by Django 4.2.16 on 2024-12-01 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0007_alter_assistentesocial_estadocivil_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitacaoAjuda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('contato', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_ajuda', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
