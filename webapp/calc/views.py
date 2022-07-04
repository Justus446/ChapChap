from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .models import Item


# Create your views here.

def index(request):
    prods = Product.objects.all()
    
    return render(request, 'index.html', {'prods': prods})


def products(request):
    items = Item.objects.all()
    return render(request, 'products.html', {'items': items})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def single(request):
    items = Item.objects.all()
    return render(request, 'single.html', {'items': items})
