from django.contrib import admin
from django.urls import path

from main.views import index, under_construction


urlpatterns = [
    path('admin/', admin.site.urls),
    # Главная
    path('', index, name='index'), 
    path('aboutdelivery/', under_construction, name='about delivery'),
    # Каталог
    path('category/<slug:category_slug>/', ProductListView.as_view(), name='category'),
    path('product/<slug:product_slug>', under_construction, name='product'),
    # Заказы
    path('orders/', under_construction, name='orders'),
    # Корзина
    path('cart/', under_construction, name='cart'),
    path('cart/checkout', under_construction, name='gocheckout'),
]
