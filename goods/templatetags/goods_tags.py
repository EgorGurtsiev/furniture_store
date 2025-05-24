from django.template import Library
from goods.models import Category

register = Library()

@register.simple_tag
def tag_category():
    return Category.objects.all()
