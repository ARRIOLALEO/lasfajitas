# Generated by Django 3.2.7 on 2021-10-04 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_categoriarestaurante'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriarestaurante',
            name='restaurante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurantes'),
        ),
    ]
