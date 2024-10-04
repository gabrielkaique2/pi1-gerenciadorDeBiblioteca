# Generated by Django 5.0.3 on 2024-10-04 00:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0007_professor_funcionario_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaLivro',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('nome_aluno', models.CharField(max_length=150)),
                ('sala', models.CharField(max_length=15)),
                ('data_reserva', models.DateField(auto_now_add=True)),
                ('livro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.livro')),
            ],
            options={
                'db_table': 'reserva_livro',
            },
        ),
        migrations.CreateModel(
            name='SugestaoLivro',
            fields=[
                ('id_sugestao', models.AutoField(primary_key=True, serialize=False)),
                ('nome_completo', models.CharField(max_length=150)),
                ('sala', models.CharField(max_length=15)),
                ('periodo', models.CharField(blank=True, max_length=50, null=True)),
                ('nome_autor', models.CharField(blank=True, max_length=255, null=True)),
                ('titulo_livro', models.CharField(max_length=255)),
                ('comentario', models.TextField(blank=True, null=True)),
                ('aluno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteca.aluno')),
            ],
            options={
                'db_table': 'sugestao_livro',
            },
        ),
    ]