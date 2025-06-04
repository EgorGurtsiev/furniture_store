from django.shortcuts import render
from django.views.generic import DetailView, ListView

from goods.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "goods/catalog.html"
    context_object_name = "products"
    
    def get_queryset(self):
        return Product.objects.in_category( # type: ignore
            slug=self.kwargs.get('category_slug')
        ).with_current_price().with_main_image()
    
    
class ProductDetailView(DetailView):
    model = Product
    template_name = "goods/product_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = self.model.objects.get_related_products(self.kwargs.get('pk'), 4
                                                                      ).with_current_price().with_main_image()
        return context
    