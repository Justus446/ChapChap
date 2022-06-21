from django.http import HttpResponse
from django.shortcuts import render
from .models import Products


# Create your views here.

def index(request):
    imgs = Products.objects.all()
    return render(request, 'index.html', {'imgs': imgs})


def products(request):
    prods = Products.objects.all()
    return render(request, 'products.html', {'prods': prods})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def single(request):
    return render(request, 'single.html')
