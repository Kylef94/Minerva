from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, default=name)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:category_list', args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    description = models.CharField('description', max_length=200)
    image = models.ImageField(upload_to='media/images/', default='media/images/default.png')
    slug = models.SlugField(max_length=255, default=name)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    created_date = models.DateTimeField("creation date", auto_now_add=True)
    last_updated = models.DateTimeField("last update date", auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'products'
        ordering = ('-created_date',)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])

    def __str__(self):
        return self.name

