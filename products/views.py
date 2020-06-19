from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello Worlds')


def productnew(request):
    return HttpResponse('Hello New Products')


def productShipping(request):
    return HttpResponse('This is a shipping page')