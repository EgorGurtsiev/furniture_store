from datetime import datetime

from factory import fuzzy
from factory.faker import Faker
from factory.django import DjangoModelFactory
from factory.declarations import SubFactory, LazyAttribute
from django.utils import timezone

from goods.models import Category, Price, Product, ProductImage


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product
    
    name = Faker('first_name')
    description = Faker('text', max_nb_chars=200)
    

class ProductImageFactory(DjangoModelFactory):
    class Meta:
        model = ProductImage
    

class PriceFactory(DjangoModelFactory):
    class Meta:
        model = Price
    
    price = fuzzy.FuzzyDecimal(1000, 100000)   
    product = SubFactory(ProductFactory)
    valid_from = fuzzy.FuzzyDateTime(
        datetime(2025, 2, 9, tzinfo=timezone.utc), 
        datetime(2025,6,29, tzinfo=timezone.utc)
    )
    valid_to = LazyAttribute(
        lambda o: fuzzy.FuzzyDateTime(
            o.valid_from, timezone.datetime.max
        )
    )



