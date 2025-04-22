from django.shortcuts import render
from django.views.generic import ListView

from goods.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "goods/catalog.html"
    context_object_name = "products"
    
    def get_queryset(self):
        # return Product.objects.by_category_slug(slug=self.kwargs.get('category_slug'))
        return Product.objects.filter(category__slug=self.kwargs.get('category_slug'))