# Generated by Django 4.2.2 on 2023-06-24 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprar',
            name='fecha_de_oferta',
            field=models.DateField(null=True),
        ),
    ]
