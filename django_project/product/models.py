from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    nome = models.CharField(max_length=30)
    quantidade = models.IntegerField()
    precoUnidade = models.DecimalField(max_digits=8, decimal_places=2)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.product_name
