from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required

from product.forms import Create_Category_Form, Create_Product_Form
from .models import Product, Category
from django.db import models


@staff_member_required
def create_category(request):

    if request.method == "POST":
        form = Create_Category_Form(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'create_category.html', {'form': form, 'all_categories': Category.objects.all()})

    else:
        form = Create_Category_Form()
        return render(request, 'create_category.html', {'form': form, 'all_categories': Category.objects.all()})



@staff_member_required
def cadastrar(request):
    if request.method == "POST":
        form = Create_Product_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('product:listproducts'))
        return render(request, 'cadastrarProduto.html', {'form': form})

    else:
        form = Create_Product_Form()
        return render(request, 'cadastrarProduto.html', {'form': form})



@staff_member_required
def edit_product(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = Create_Product_Form(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('products:list_products'))
        return render(request, 'edit_products.html', {'form': form})

    else:
        form = Create_Product_Form(instance=product)
        return render(request, 'edit_products.html', {'form': form})

def list_products(request):
    context = {
        'all_products': Product.objects.all(),
    }
    return render(request, 'list_products.html', context)

@staff_member_required
def delete_products(request, product_id):
    Product.objects.get(id=product_id).delete()
    return HttpResponseRedirect(reverse('product:listproducts'))
