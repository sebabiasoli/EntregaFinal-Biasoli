# Generated by Django 4.2.2 on 2023-07-08 21:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_delete_comprar_vender_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='vender',
            name='vendedor',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
