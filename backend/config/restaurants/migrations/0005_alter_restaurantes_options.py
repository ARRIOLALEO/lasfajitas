# Generated by Django 3.2.7 on 2021-10-02 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_alter_restaurantes_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurantes',
            options={'verbose_name': 'Restaurantes', 'verbose_name_plural': 'Restaurantes'},
        ),
    ]