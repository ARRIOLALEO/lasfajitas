# Generated by Django 3.2.7 on 2021-10-02 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantes',
            name='descripcion',
            field=models.TextField(help_text='aqui ingrese el numbe rel restaurante', null=True, verbose_name='Descripcion del Restaurante'),
        ),
        migrations.AddField(
            model_name='restaurantes',
            name='imagen_del_restaurante',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='restaurantes',
            name='restaurante',
            field=models.CharField(blank=True, help_text='Ingrese el Nombre del Restaurante', max_length=300, null=True, verbose_name='Nombre del Restaurante'),
        ),
    ]
