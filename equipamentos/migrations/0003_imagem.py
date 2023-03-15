# Generated by Django 4.1.7 on 2023-03-15 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0002_remove_equipamento_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='images')),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipamentos.equipamento')),
            ],
        ),
    ]
