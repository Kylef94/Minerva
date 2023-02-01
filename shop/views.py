from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Category, Product

def home(request):
    return HttpResponse("Hello, World. Welcome to Minerva")

def product_all(request):
    #products = Product.products.all() {'products': products}
    return render(request, 'shop/home.html')
