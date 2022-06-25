from django.db import models


# Create your models here.
class Product(models.Model):
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()


class Item(models.Model):
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
