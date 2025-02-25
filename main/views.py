from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


def under_construction(request):
    return render(request, 'main/503.html', status=503)


def index(request):
    context = {
        'title': 'NailFurni',
    }
    return render(request, 'main/index.html', context)