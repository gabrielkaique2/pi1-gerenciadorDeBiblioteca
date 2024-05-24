# Generated by Django 5.0.3 on 2024-05-24 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_remove_professor_funcionario_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor_funcionario',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='professor_funcionario',
            name='telefone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
