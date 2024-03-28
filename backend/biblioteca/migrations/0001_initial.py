# Generated by Django 5.0.3 on 2024-03-27 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id_aluno', models.AutoField(primary_key=True, serialize=False)),
                ('nome_do_aluno', models.CharField(max_length=150)),
                ('ra', models.CharField(max_length=15, null=True)),
                ('serie', models.CharField(max_length=10, null=True)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'aluno',
            },
        ),
        migrations.CreateModel(
            name='Nicho',
            fields=[
                ('id_nicho', models.BigAutoField(primary_key=True, serialize=False)),
                ('numero_nicho', models.PositiveIntegerField()),
                ('local', models.CharField(max_length=100, null=True)),
                ('observacao', models.TextField(null=True)),
            ],
            options={
                'db_table': 'nicho',
            },
        ),
        migrations.CreateModel(
            name='StatusEmprestimo',
            fields=[
                ('id_status', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Emprestado', 'Emprestado'), ('Devolvido', 'Devolvido'), ('Extraviado', 'Extraviado'), ('Reservado', 'Reservado'), ('Aguardando_retirada', 'Aguardando Retirada'), ('Em_processamento', 'Em Processamento'), ('Vencido', 'Vencido'), ('Renovado', 'Renovado'), ('Danificado', 'Danificado'), ('Em_analise', 'Em Análise'), ('Cancelado', 'Cancelado')], max_length=20)),
            ],
            options={
                'db_table': 'statusemprestimo',
            },
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id_emprestimo', models.AutoField(primary_key=True, serialize=False)),
                ('data_emprestimo', models.DateField()),
                ('data_devolucao', models.DateField()),
                ('id_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.aluno')),
            ],
            options={
                'db_table': 'emprestimo',
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id_livro', models.AutoField(primary_key=True, serialize=False)),
                ('nome_do_livro', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=100, null=True)),
                ('quantidade_exemplar', models.IntegerField()),
                ('saldo_exemplar', models.IntegerField()),
                ('observacao_livro', models.TextField(null=True)),
                ('id_nicho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.nicho')),
            ],
            options={
                'db_table': 'livro',
            },
        ),
        migrations.CreateModel(
            name='LivroEmprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('id_emprestimo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.emprestimo')),
                ('id_livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.livro')),
                ('id_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.statusemprestimo')),
            ],
            options={
                'db_table': 'livro_emprestimo',
                'unique_together': {('id_livro', 'id_emprestimo')},
            },
        ),
    ]