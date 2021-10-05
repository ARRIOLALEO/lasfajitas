from django.contrib import admin
from .models import Restaurantes, CategoriaRestaurante, Producto,Conductor,Order
# Register your models here.

admin.site.register([Restaurantes,CategoriaRestaurante,Producto, Conductor,Order])

