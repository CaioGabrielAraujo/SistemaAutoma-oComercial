from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    nome = models.CharField(max_length=30)
    quantidade = models.IntegerField()
    precoUnidade = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome
