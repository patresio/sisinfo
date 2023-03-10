# Generated by Django 4.1.7 on 2023-03-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diretorias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diretoria',
            name='tipo',
            field=models.CharField(choices=[('1', 'Gabinete'), ('2', 'Departamento'), ('3', 'Diretoria'), ('4', 'Secretaria')], default='3', max_length=1),
        ),
    ]