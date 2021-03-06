# Generated by Django 3.2.7 on 2021-10-04 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_categoriarestaurante_restaurante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, help_text='ingrese eL nombre del Producto', max_length=250, null=True, verbose_name='Nombre del Producto')),
                ('esta_disponible', models.IntegerField(choices=[(2, 'SI'), (2, 'NO')])),
                ('descripcion', models.TextField(blank=True, help_text='ingrese el la descripcion', null=True, verbose_name='Descripcion Del Producto')),
                ('precio', models.FloatField()),
                ('image_princial', models.ImageField(upload_to='', verbose_name='Agrege la imagen pricipal del Producto')),
                ('imagen_dos', models.ImageField(blank=True, null=True, upload_to='', verbose_name='agrege imagen opcional')),
                ('image_tres', models.ImageField(blank=True, null=True, upload_to='', verbose_name='agrege imagen opcional')),
                ('image_cuatro', models.ImageField(blank=True, null=True, upload_to='', verbose_name='agrege imagen opcional')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.categoriarestaurante')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
