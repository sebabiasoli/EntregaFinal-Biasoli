# Generated by Django 4.2.3 on 2023-07-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='description',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='page_link',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='user',
        ),
        migrations.AddField(
            model_name='perfil',
            name='first_name',
            field=models.CharField(default='Valor predeterminado', max_length=20, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='last_name',
            field=models.CharField(default='Valor predeterminado', max_length=20, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
