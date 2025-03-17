from django.shortcuts import render
from django.views.generic import ListView

from goods.models import Product


class CatalogView(ListView):
    model = Product
    template_name = "goods/catalog.html"
    context_object_name = "products"
