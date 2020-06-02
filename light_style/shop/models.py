from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='img')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    height = models.CharField(max_length=4)
    width = models.CharField(max_length=4)
    manufacturer = models.CharField(max_length=50)              # производитель
    reinforcement_material = models.CharField(max_length=100)   # материал арматуры
    power = models.CharField(max_length=30)                     # Мощность
    armature_color = models.CharField(max_length=100)           # Цвет арматуры
    lighting_area = models.CharField(max_length=20)             # Площадь освещения
    number_of_lamps = models.CharField(max_length=5)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Photo(models.Model):
    product = models.ForeignKey(Product, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img")
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'create_at'
        ordering = ['create_at']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f"{self.product.name} photo"

