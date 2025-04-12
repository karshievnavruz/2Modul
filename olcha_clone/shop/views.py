# shop/views.py
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()  # Barcha mahsulotlar
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id=id)  # Mahsulotning detallari
    return render(request, 'shop/product_detail.html', {'product': product})
