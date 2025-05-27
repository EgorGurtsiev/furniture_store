from factory.django import DjangoModelFactory

from carts.models import CartItem




class CartItemFactory(DjangoModelFactory):
    class Meta:
        model = CartItem
    
