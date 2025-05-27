from rest_framework.serializers import ModelSerializer, Serializer

from carts.models import CartItem, Cart


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
        
        
class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"
        
        
class AddToCartSerializer(Serializer):
    pass