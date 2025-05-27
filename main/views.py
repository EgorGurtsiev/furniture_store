from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

from goods.models import Product


def under_construction(request, *args, **kwargs):
    return render(request, 'main/503.html', status=503)


def index(request):
    context = {
        'title': 'NailFurni',
        'products': Product.objects.all().with_main_image().with_current_price()
    }
    return render(request, 'main/index.html', context)