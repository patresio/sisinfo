# Generated by Django 4.1.7 on 2023-03-15 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0002_remove_equipamento_album'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Imagem',
        ),
        migrations.DeleteModel(
            name='ImagemAlbum',
        ),
    ]