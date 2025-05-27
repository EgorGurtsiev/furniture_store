from django.urls import reverse
from django.views.generic import FormView, TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from carts.models import Cart, CartItem
from carts.serializers import CartItemSerializer, CartSerializer


class CartView(ListView):
    template_name = 'carts/cart.html'
    queryset = CartItem.objects.all()
    context_object_name = 'cart_items'
    
    def get_queryset(self):
        return super().get_queryset().filter(cart__user = self.request.user)
    


class CartModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer
    lookup_field = 'pk'
    
    
class CartItemModelViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'path', 'delete',]
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer
    lookup_field = 'product'
    queryset = CartItem.objects.all()
    
    def get_queryset(self):
        return super().get_queryset().filter(cart__user=self.request.user)
   
    def get_cart(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
   
    def perform_create(self, serializer):
        cart = self.get_cart()
        product = serializer.validated_data['product']
        
        # Проверяем, есть ли уже такой товар в корзине
        cart_item = CartItem.objects.filter(cart=cart, product=product)
        if cart_item.exists():
            return
        else:
            serializer.save(cart=cart, quantity=1)
   
    # @action(methods='post', detail=True, url_path='add', url_name='increment')
    # def increment(self, request, *args, **kwargs):
    #     """Добавляет 1 к quantity""" 
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)   
    #     cart_item = self.get_object()
    #     if cart_item.quantity > 1:
    #         cart_item.quantity -= 1
    #         cart_item.save()
    #         serializer = self.get_serializer(cart_item)
    #         return Response(serializer.data)
    #     else:
    #         cart_item.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    
    # @action(methods='post', detail=True, url_path='reduce', url_name='decrement')
    # def decrement(self):
    #     """Уменьшает quantity на 1. Следит, чтобы quantity не опускалось ниже 1""" 
    #     instance = self.get_object()
    #     instance
    #     serializer = self.get_serializer(instance, data={'quantity': 1,}, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)

    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}

    #     return Response(serializer.data)
    
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']
    
    # def create(self, request, *args, **kwargs):
    #     """Создает новую запись или добавляет присланное количество к текущему в БД"""
    #     cart, _ = Cart.objects.get_or_create(user=request.user)
    #     serializer = AddToCartSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
        
    #     quantity = serializer.validated_data['quantity'] 
    #     cart_item, created = CartItem.objects.get_or_create(
    #         cart=cart,
    #         product=serializer.validated_data['product_id'],
    #         defaults={'quantity': quantity }
    #     )

    #     if not created:
    #         cart_item.quantity += quantity
    #         cart_item.save()

    #     # return Response(self.get_serializer(cart).data, status=status.HTTP_201)
        
