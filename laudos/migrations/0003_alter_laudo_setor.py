# Generated by Django 4.1.7 on 2023-03-26 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setores', '0001_initial'),
        ('laudos', '0002_alter_laudomaterial_numero_laudo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laudo',
            name='setor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='setores.setor'),
        ),
    ]
