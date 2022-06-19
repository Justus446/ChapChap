from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('contact', views.contact, name='contact'),
    path('single', views.single, name='single'),
    path('about', views.about, name='about')
]
