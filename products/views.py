from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    product = Product.objects.all()
    return render(request,
                  'index.html',
                  {'products': product})


def productnew(request):
    return HttpResponse('Hello New Products')


def productShipping(request):
    return HttpResponse('This is a shipping page')