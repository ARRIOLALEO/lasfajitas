# Generated by Django 3.2.7 on 2021-10-04 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_alter_restaurantes_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaRestaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(blank=True, help_text='ingrese el nombre de la catgoria', max_length=300, null=True, verbose_name='Nombre de la categoria')),
                ('descripcion', models.TextField(blank=True, help_text='ingrese la descripcion de la categoria', null=True, verbose_name='Descripcion de la categoria')),
                ('slider_de_la_sub_categoria', models.ImageField(null=True, upload_to='')),
                ('descripcion_slider', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]