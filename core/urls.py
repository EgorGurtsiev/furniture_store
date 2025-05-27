from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework.routers import DefaultRouter

from carts.views import CartItemModelViewSet, CartModelViewSet, CartView
from goods.views import ProductDetailView, ProductListView
from main.views import index, under_construction
# from orders.views import OrderListView, OrderDetailView


router = DefaultRouter()

# Заказы
router.register('cart_items', CartItemModelViewSet, 'cart_items')
router.register('cart', CartModelViewSet, 'cart')

urlpatterns = [
    path('admin/', admin.site.urls),
    # Главная
    path('', index, name='index'), 
    path('aboutdelivery/', under_construction, name='about delivery'),
    # Каталог
    path('category/<slug:category_slug>/', ProductListView.as_view(), name='category'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product'),
    # Заказы
    # path('orders/', OrderListView.as_view(), name='orders'), # Все заказы пользователя
    # path('orders/<int:pk', OrderDetailView.as_view(), name='order'), # Конкретный заказ пользователя
    # Корзина
    path('cart/', CartView.as_view(), name='cart'),
    # path('cart/checkout', under_construction, name='gocheckout'),
    # Аккаунт
    path('account/', include("django.contrib.auth.urls")),
    # path('account/login', under_construction, name='login'),
    # path('account/logout', under_construction, name='logout'),
    # path('account/register', under_construction, name='register'),
    # API
    path('api/', include(router.urls))
]  + debug_toolbar_urls()


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
