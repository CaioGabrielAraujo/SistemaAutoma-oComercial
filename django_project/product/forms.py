from django import forms
from django.forms import ModelForm
from .models import Product, Category, Venda



class Create_Product_Form(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'nome': 'Nome do Produto',
            'precoUnidade': 'Preco',
            'quantidade': 'Quantidade',
            'categories': 'Categoria',

        }

        widgets = {
            'categories': forms.CheckboxSelectMultiple()
        }


class Create_Category_Form(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'category_name': 'Nome da Categoria',
        }

class Create_Venda_Form(ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'
        labels = {
            'descricao': 'Descricao',
            'produtos': 'Produtos',
        }
        widgets = {
            'produtos': forms.CheckboxSelectMultiple()
        }
