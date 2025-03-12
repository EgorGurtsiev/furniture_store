from django.contrib import admin

from goods.models import Product, ProductGroup


@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    list_display= ['name', 'parent']
    prepopulated_fields={'slug': ( 'name', )}
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= ['name']