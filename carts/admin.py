from django.contrib import admin

from carts.models import Cart, CartItem


class CartItemsInline(admin.TabularInline):
    model = CartItem
    extra = 1
    fields = ('product', 'quantity',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user',]
    inlines = [CartItemsInline,]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'get_cart_user',)
    list_filter = ('product','cart__user',)
    
    def get_cart_user(self, obj):
        return obj.cart.user if obj.cart else None
    
    get_cart_user.short_description = 'Пользователь'
    get_cart_user.admin_order_field = 'cart__user'