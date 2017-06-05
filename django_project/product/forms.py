from django import forms
from django.forms import ModelForm
from .models import Product, Category

class Create_Product_Form(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_name': 'Nome do Produto',
            'price': 'Preco',
            'description': 'Descricao',
            'amount': 'Quantidade',

        }

class Create_Category_Form(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'category_name': 'Nome da Categoria'
        }
