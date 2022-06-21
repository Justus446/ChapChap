from django.db import models


# Create your models here.
class Products(models.Model):
    img = models.ImageField(upload_to='images')
    desc = models.TextField()
    price = models.IntegerField()


class Items(models.Model):
    img = models.ImageField(upload_to='images')
    desc = models.TextField()
    price = models.IntegerField()
