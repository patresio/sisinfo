# Generated by Django 4.1.7 on 2023-03-28 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suprimentos', '0001_initial'),
        ('laudos', '0004_alter_laudomaterial_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laudomaterial',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='suprimentos.material'),
        ),
    ]
