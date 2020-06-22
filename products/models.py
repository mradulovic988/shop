from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=255)


class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Cart(models.Model):
    price = models.FloatField()
    productName = models.CharField(max_length=100)
    userName = models.CharField(max_length=50)
    userEmail = models.EmailField()
    userAddress = models.CharField(max_length=255)

