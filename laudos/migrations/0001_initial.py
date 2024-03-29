# Generated by Django 4.1.7 on 2023-03-24 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suprimentos', '0001_initial'),
        ('setores', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Laudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacao', models.CharField(blank=True, max_length=24, null=True)),
                ('funcionario', models.CharField(blank=True, max_length=200, null=True)),
                ('justificativa', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('01', 'Aberto'), ('02', 'Em andamento'), ('03', 'Finalizado')], default='01', max_length=2, null=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True, null=True)),
                ('profissional', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('setor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='setores.setor')),
            ],
        ),
        migrations.CreateModel(
            name='LaudoMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True, default=0, null=True)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='suprimentos.material')),
                ('numero_laudo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='laudos.laudo')),
            ],
        ),
    ]
