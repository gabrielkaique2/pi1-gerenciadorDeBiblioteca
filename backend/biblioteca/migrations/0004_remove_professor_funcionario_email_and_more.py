# Generated by Django 5.0.3 on 2024-05-24 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_remove_aluno_ativo_remove_aluno_data_registro_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor_funcionario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='professor_funcionario',
            name='telefone',
        ),
    ]
