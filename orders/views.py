# from django.views.generic import ListView, DetailView

# from orders.models import Order


# class OrderListView(ListView):
#     """Список заказов пользователя"""
#     model = Order
#     template_name = "orders/order_list.html"
    
#     def get_queryset(self):
#         return super().get_queryset().filter(user=self.request.user)


# class OrderDetailView(DetailView):
#     """Заказ"""
#     model = Order
#     template_name = "orders/order_detail.html"