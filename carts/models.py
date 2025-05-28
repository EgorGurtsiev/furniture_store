from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

from goods.models import Product

user = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(user, models.CASCADE, related_name='cart', verbose_name='Владелец(пользователь)')
    
    def __str__(self) -> str:
        return f"Корзина пользователя {self.user}"
    
    class Мета:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartItemManager(models.Manager):
    def total_price(self):
        return sum(obj.quantity * obj.product.get_current_price() for obj in self.get_queryset())

    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, models.CASCADE, related_name='cart_items')
    quantity = models.IntegerField('Количество', validators=[MinValueValidator(1)])
    
    objects = CartItemManager()
    
    @property
    def total_price(self):
        price = self.product.price
        if not price:
            return None
        return self.quantity * price.price         
    
    def __str__(self) -> str:
        return f"{self.quantity} x {self.product.name} в корзине пользователя {self.cart.user}"
    
    class Мета:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'