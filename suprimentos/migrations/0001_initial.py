# Generated by Django 4.1.7 on 2023-03-15 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessoLicitatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('1', 'Ativo'), ('2', 'Inativo')], default=1, max_length=1)),
            ],
            options={
                'verbose_name': 'Processo',
                'verbose_name_plural': 'Processos',
                'ordering': ('status',),
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('1', 'Ativo'), ('2', 'Inativo')], default=1, max_length=1)),
                ('proc_licitatorio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='materiais', to='suprimentos.processolicitatorio', verbose_name='processo')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiais',
                'ordering': ('status', 'proc_licitatorio', 'nome'),
            },
        ),
        migrations.CreateModel(
            name='CPUCompleto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('1', 'Ativo'), ('2', 'Inativo')], default=1, max_length=1)),
                ('pecas', models.ManyToManyField(to='suprimentos.material')),
                ('proc_licitatorio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suprimentos.processolicitatorio')),
            ],
        ),
    ]
