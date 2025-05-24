from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings
from goods.views import ProductDetailView, ProductListView
from main.views import index, under_construction
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    # Главная
    path('', index, name='index'), 
    path('aboutdelivery/', under_construction, name='about delivery'),
    # Каталог
    path('category/<slug:category_slug>/', ProductListView.as_view(), name='category'),

    path('product/<slug:slug>', ProductDetailView.as_view(), name='product'),
    # Заказы
    path('orders/', under_construction, name='orders'),
    # Корзина
    path('cart/', under_construction, name='cart'),
    path('cart/checkout', under_construction, name='gocheckout'),
]  + debug_toolbar_urls()



# if settings.DEBUG: # new
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)