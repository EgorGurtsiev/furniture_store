from django.shortcuts import render
from django.views.generic import DetailView, ListView

from goods.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "goods/catalog.html"
    context_object_name = "products"
    
    def get_queryset(self):
        return Product.objects.in_category(
            slug=self.kwargs.get('category_slug')
        ).with_current_price().with_main_image()
    
    
class ProductDetailView(DetailView):
    model = Product
    template_name = "goods/product_detail.html"