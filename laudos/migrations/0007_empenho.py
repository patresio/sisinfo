# Generated by Django 4.1.7 on 2023-04-12 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laudos', '0006_alter_laudo_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empenho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_empenho', models.CharField(blank=True, max_length=10, null=True)),
                ('fornecedor', models.CharField(blank=True, max_length=255, null=True)),
                ('nota_fiscal', models.CharField(blank=True, max_length=10, null=True)),
                ('numero_laudo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='empenhos', to='laudos.laudo')),
            ],
        ),
    ]