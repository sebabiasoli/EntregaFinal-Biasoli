# Generated by Django 4.2.2 on 2023-06-25 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_alter_comprar_fecha_de_oferta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('fecha_de_oferta', models.DateField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Comprar',
        ),
    ]
