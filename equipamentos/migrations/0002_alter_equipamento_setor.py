# Generated by Django 4.1.7 on 2023-03-14 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setores', '0003_alter_setor_options'),
        ('equipamentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='setor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='setores.setor'),
        ),
    ]
