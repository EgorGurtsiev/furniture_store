from django.template import Library

from goods.models import ProductGroup

register = Library()

@register.simple_tag
def tag_product_group():
    return ProductGroup.objects.all()