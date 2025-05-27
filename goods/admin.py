from django.contrib import admin
from django.utils.safestring import mark_safe

from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin
# from eav.models import Attribute, Value, EnumGroup, EnumValue

from goods.models import Product, Category, ProductImage, Price

# admin.site.unregister(Attribute)
# admin.site.unregister(Value)
# admin.site.unregister(EnumGroup)
# admin.site.unregister(EnumValue)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ['name', 'parent']
    prepopulated_fields={'slug': ( 'name', )}


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('original',)
    readonly_fields = ('thumbnail', 'medium')


class ProductAdminForm(BaseDynamicEntityForm):
    model = Product


@admin.register(Product)
class ProductAdmin(BaseEntityAdmin):
    list_display = ('name', 'category')
    form = ProductAdminForm
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'get_thumbnail',)
    list_filter = ('product', 'is_main')
    
    def get_thumbnail(self, obj):
        return mark_safe(f'<img src={obj.thumbnail.url} high="30" width="40">')
    
    get_thumbnail.short_description = 'Иконка'
   
    
@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('price', 'product', 'valid_from', 'valid_to')
    list_filter = ('product',)
    