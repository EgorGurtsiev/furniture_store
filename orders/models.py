# from django.contrib.auth import get_user_model
# from django.core.validators import MinValueValidator
# from django.db import models
# from django.urls import reverse

# from goods.models import Product


# class OrderStatus(models.Model):
#     name = models.CharField(max_length=50, verbose_name='Название статуса заказа')
#     code = models.SlugField(unique=True, verbose_name='Код статуса заказа')
    
#     class Meta:
#         verbose_name = 'Статус заказа'
#         verbose_name_plural = 'Статусы заказов'
    
#     def __str__(self):
#         return f'Статус заказа {self.name} - код {self.code}'


# class Order(models.Model):
#     user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
#     created_at = models.DateTimeField("Дата создания заказа", auto_now_add=True)
#     status  = models.ForeignKey(OrderStatus, on_delete=models.PROTECT, related_name='orders')

#     class Meta:
#         verbose_name = "Заказ"
#         verbose_name_plural = "Заказы"

#     def __str__(self):
#         return f'Корзина пользователя {self.user}'

#     def get_absolute_url(self):
#         return reverse("order", kwargs={"pk": self.pk})

 
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
#     quantity = models.IntegerField('Количество', validators=[MinValueValidator(1)])
    
#     class Meta:
#         verbose_name = "Элемент заказа"
#         verbose_name_plural = "Элементы заказа"

#     def __str__(self):
#         return f'{self.Meta.verbose_name} {self.order.pk} - {self.quantity} шт. {self.product}'