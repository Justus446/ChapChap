from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html', {'name': 'shakira', 'husband': 'Pique'})


def shape(request):
    forehead = int(request.POST["forehead"])
    chin = int(request.POST["chin"])
    jaw = int(request.POST["jaw"])
    res = 'no shape'

    if jaw < forehead > chin:
        res = 'triangle'
    if jaw < chin > forehead:
        res = 'diamond'
    if jaw == forehead == chin:
        res = 'square'

    return render(request, 'shape.html', {'shape': res})


def index(request):
    return render(request, 'index.html')
