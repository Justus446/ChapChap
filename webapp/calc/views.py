from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .models import Item


# Create your views here.

def index(request):
    imgs = Product.objects.all()
    
    return render(request, 'index.html', {'imgs': imgs})


def products(request):
    prods = Item.objects.all()
    return render(request, 'products.html', {'prods': prods})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def single(request):
    return render(request, 'single.html')
