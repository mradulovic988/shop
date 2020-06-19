from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.productnew),
    path('shipping', views.productShipping)
]