from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name= 'Categoría')
    descripcion = models.TextField(blank=True, null=True, max_length=200, verbose_name= 'Descripción')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name= 'Producto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    fecha_ingreso = models.DateField(auto_now_add=True, verbose_name= 'Fecha de ingreso')
    stock_prod = models.IntegerField(default=0, verbose_name='Stock disponible')
    disponible = models.BooleanField(default=True, verbose_name='¿Esta disponible?')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'