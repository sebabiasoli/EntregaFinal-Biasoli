# Generated by Django 4.2.3 on 2023-07-09 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_remove_perfil_description_remove_perfil_page_link_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]
