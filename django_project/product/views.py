from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .models import Product
from django.db import models



def cadastrar(request):
    if request.method == "GET":
        return render(request, 'cadastrarProduto.html')
    else:
        form = request.POST
        nome = form.get('Nomedoproduto')
        quantidade = form.get('Quantidade')
        preco = float(form.get('Preco'))



        product = Product(nome=nome, quantidade=quantidade, precoUnidade=preco)
        product.save()


    return render(request, 'index.html')


def list_products(request):
    context = {
        'all_products': Product.objects.all(),
    }
    return render(request, 'list_products.html', context)
