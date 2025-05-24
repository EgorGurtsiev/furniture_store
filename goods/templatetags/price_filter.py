from django import template

register = template.Library()

@register.filter(name='price_format')
def price_format(price):
    """
    Форматирует float в строку формата "12 345,67 ₽"
    """
    if price:
        return "{:,.2f} ₽".format(float(price)).replace(",", " ").replace(".", ",")
    else:
        return price
