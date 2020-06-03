from django.shortcuts import render, redirect
from shop.models import Product, Category


def catalog(request):
    products = Product.objects.all()
    return render(request, 'products.html', context={'products': products})


def retrieve(request, id=None):
    product = Product.objects.get(pk=id)
    return render(request, 'retrieve.html', context={'product': product})

