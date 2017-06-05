from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import Create_Product_Form
from .models import Product, Category



def cadastrar(request):
    if request.method == "POST":
        form = Create_Product_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'cadastrarProduto.html', {'form': form})

    else:
        form = Create_Product_Form()
        return render(request, 'cadastrarProduto.html', {'form': form})


def list_products(request):
    context = {
        'all_products': Product.objects.all(),
    }
    return render(request, 'list_products.html', context)

def create_category(request):

    if request.method == "POST":
        form = Create_Category_Form(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'createCategory/create_category.html', {'form': form, 'all_categories': Category.objects.all()})

    else:
        form = Create_Category_Form()
        return render(request, 'createCategory/create_category.html', {'form': form, 'all_categories': Category.objects.all()})

def delete_categories(request, category_id):
        Category.objects.get(id=category_id).delete()
        return HttpResponseRedirect(reverse('products:create_category'))
