# Generated by Django 4.1.7 on 2023-03-13 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suprimentos', '0004_cpucompleto'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpucompleto',
            name='status',
            field=models.CharField(choices=[('1', 'Ativo'), ('2', 'Inativo')], default=1, max_length=1),
        ),
    ]
