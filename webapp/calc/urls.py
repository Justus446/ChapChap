from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('contact', views.contact, name='contact'),
    path('single-product', views.single, name='single-product'),
    path('about', views.shape, name='about')
]
