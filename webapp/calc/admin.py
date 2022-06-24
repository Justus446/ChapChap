from django.contrib import admin
from .models import Products
from .models import Items

# Register your models here.
admin.site.register(Products)
admin.site.register(Items)
