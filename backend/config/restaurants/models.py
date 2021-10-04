from django.db import models
from django.db.models.enums import Choices

# Create your models here.

class Restaurantes(models.Model):
    restaurante = models.CharField(max_length=300,verbose_name=u"Nombre del Restaurante", help_text=u"Ingrese el Nombre del Restaurante",blank=True, null=True)
    descripcion = models.TextField(verbose_name="Descripcion del Restaurante", help_text="aqui ingrese el numbe rel restaurante", null=True)
    imagen_del_restaurante = models.ImageField(null=True)
    slider_Del_restaurante = models.ImageField(null= True)
    descripcion_slider = models.CharField(max_length=250,verbose_name=u"aqui va la informacion del slider",help_text="descripcion del slider",blank=True, null=True)

    def __get__label(self):
        return text_type(self.__meta.get_field(field).verbose_name)

    def __str__(self):
        return  self.restaurante

    class Meta:
        verbose_name = "Restaurantes"
        verbose_name_plural = "Restaurantes"

class CategoriaRestaurante(models.Model):
    categoria = models.CharField(max_length=300, verbose_name=u"Nombre de la categoria", help_text=U"ingrese el nombre de la catgoria",blank=True ,null=True)
    restaurante= models.ForeignKey(Restaurantes,on_delete=models.CASCADE,blank=True,null=True)
    descripcion = models.TextField(verbose_name="Descripcion de la categoria",help_text="ingrese la descripcion de la categoria", blank= True, null=True)
    slider_de_la_sub_categoria = models.ImageField(null=True)
    descripcion_slider =  models.TextField(null=True)


    def __get__label(self):
        return text_type(self.__meta.get_field(field).verbose_name)
    def __str__(self):
        return  self.categoria

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Producto(models.Model):
    choices_yes_not =[(2,"SI"),(2,"NO"),]
    nombre  = models.CharField(max_length=250, verbose_name=u"Nombre del Producto",help_text=U"ingrese eL nombre del Producto", blank=True, null=True)
    categoria = models.ForeignKey(CategoriaRestaurante,on_delete=models.CASCADE,blank=True,null= True)
    esta_disponible = models.IntegerField(choices=choices_yes_not)
    descripcion = models.TextField(verbose_name=u"Descripcion Del Producto", help_text=u"ingrese el la descripcion", blank=True, null=True)
    precio = models.FloatField(null=False)
    image_princial = models.ImageField(verbose_name=u"Agrege la imagen pricipal del Producto",null=False)
    imagen_dos = models.ImageField(verbose_name=u"agrege imagen opcional",blank=True, null=True)
    image_tres = models.ImageField(verbose_name=u"agrege imagen opcional", blank=True, null=True)
    image_cuatro = models.ImageField(verbose_name=u"agrege imagen opcional", blank=True, null= True)

    def __get__label(self):
        return text_type(Self.__meta.get_field(field).verbose_name)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name= "Product"
        verbose_name_plural = "Products"
