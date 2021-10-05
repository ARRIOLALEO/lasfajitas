from django.db import models
from django.db.models.fields.related import ForeignKey

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
    choices_yes_not =[(1,"SI"),(2,"NO"),]
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
        return text_type(self.__meta.get_field(field).verbose_name)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name= "Product"
        verbose_name_plural = "Products"

class Conductor(models.Model):
    esta_disponible = [(1,"SI"),(2,"NO")]
    name= models.CharField(max_length=250, verbose_name=u"Nombre del Conductor", help_text=u"agrege el numbre del conductor", blank=True, null =True)
    telefon = models.IntegerField( verbose_name=u"ingrese el numero de contacto" , help_text=u"agrege el numero telefonico", blank=True,null=True)
    direcction = models.TextField(verbose_name=u"agrege la direcion del conductor",help_text=u"agrege la direcion", blank=True,null=True)
    esta_disponible = models.IntegerField(choices=esta_disponible)

    def __get__label(self):
        return text_type(self.__meta.get_field(field).verbose_name)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Conductor"
        verbose_name_plural = "Conductores"

class Order(models.Model):
    departamentos = [(1,"San Salvador")]
    ciudades =[(1,"San Salvador"),(2,"otra ciudad")]
    opciones =[(1,"Delivery"),(2,"Recoger en Tienda")]
    estado_de_order = [(1,"realizada"),(2,"en cocina"),(3,"en delivery"),(4,"entregada"),(5,"anulada")]
    restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE,blank=True,null=True)
    tiempo_order_realizada = models.DateTimeField(auto_now_add=True)
    nombres = models.CharField(max_length=250, verbose_name=u"nombre del cliente",help_text=u"here goes the name of the customer", blank=True, null=True)
    apellidos = models.CharField(max_length=250,verbose_name=u"appellidos del cliente",help_text=u" here goes the lastnames of the customer",blank=True, null=True)
    numero_telefono = models.IntegerField(max_length=10,verbose_name=u"ingrese nuero de client",help_text=u"aqui va el el telefono del cliente",blank=True,null=True)
    correo_elect = models.EmailField(verbose_name="Correo Electronico",help_text=u"este es el email")
    departament = models.IntegerField(choices=departamentos)
    direccion_uno = models.CharField(max_length=250,verbose_name=u"dereccion 1", help_text=u"aqui va la direccion 1", blank=True, null=True)
    direccion_dos = models.CharField(max_length=250,verbose_name=u"direccion 2", help_text=u"aqui va la direccion 2",blank=True,null=True)
    ciudad = models.IntegerField(choices=ciudades)
    opciones_entrega = models.IntegerField(choices=opciones,verbose_name=u"opcion selecionada por el cliente")
    notas = models.TextField()
    conductor = models.ForeignKey(Conductor,on_delete=models.DO_NOTHING)
    estado_de_la_orden = models.IntegerField(choices=estado_de_order)

    def __get__label(self):
        return text_type(self.__meta.get_field(field).verbose_name)

    def __str__(self):
        return self.nombres
    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes"






