from datetime import datetime
from django.db import models
from django.db.models import Prefetch
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill
from tree_queries.models import TreeNode
from uuid import uuid4
from eav.decorators import register_eav
from eav.registry import EavConfig


class Category(TreeNode):
    slug=models.SlugField(max_length=255, unique=True, null=False, db_index=True)
    name=models.CharField(verbose_name="Название", max_length=255, db_index=True)
    
    def _get_new_slug(self) -> str:
        return f"{slugify(self.name)}"
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})
        
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Категория"
        verbose_name_plural="Категории"


class ProductQuerySet(models.QuerySet):
    def with_main_image(self):
        return self.prefetch_related(
            Prefetch('images', ProductImage.objects.main())
        )
    
    def with_current_price(self):
        return self.prefetch_related(
            Prefetch('prices', Price.objects.current().only('product', 'price'))
        )
    
    def in_category(self, slug:str) -> models.QuerySet:
        """Фильтрация товаров по категории

        Args:
            slug (str): slug категории искомых товаров

        Returns:
            models.QuerySet: Товары в указанной категории
        """
        return self.filter(category__slug=slug)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def with_current_price(self):
        return self.get_queryset().with_current_price()
    
    def in_category(self, slug:str) -> models.QuerySet:
        """Фильтрация товаров по категории

        Args:
            slug (str): slug категории искомых товаров

        Returns:
            models.QuerySet: Товары в указанной категории
        """
        return self.get_queryset().in_category(slug=slug)


class ProductEavConfig(EavConfig):
    manager_attr = 'eav_objects'


@register_eav(config_cls=ProductEavConfig)
class Product(models.Model):
    slug=models.SlugField(max_length=255, unique=True, db_index=True)
    name=models.CharField(verbose_name="Название", max_length=255, db_index=True)
    category=models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    description=models.CharField(max_length=1275, default='')
    
    objects=ProductManager()
    
    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = f"{slugify(self.name)}-{uuid4().hex[:6]}"
       super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Товар"
        verbose_name_plural="Товары"
       
       
class ProductImageManager(models.Manager):
    def main(self):
        return self.get_queryset().filter(is_main=True) 

    
class ProductImage(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    original=models.ImageField(verbose_name="Изображение", upload_to='product/original')
    thumbnail=ImageSpecField(
        source="original",
        processors=[ResizeToFill(200, 150)],
        format='JPEG',
        options={'quality': 80},
    )
    medium=ImageSpecField(
        source="original",
        processors=[ResizeToFill(400, 300)], 
        format='JPEG',
        options={'quality': 80},
    )
    is_main = models.BooleanField(verbose_name="Главное изображение", default=False)
    
    objects = ProductImageManager()
    
    def __str__(self):
        return f"Изображение для {self.product.name}"
    
    class Meta:
        verbose_name="Изображение товар"
        verbose_name_plural="Изображения товаров"


class PriceQuerySet(models.QuerySet):
    def get_current_price(self):
        now = timezone.now()
        return self.filter(
            valid_from__lte=now, 
            valid_to__gte=now
        ).order_by('product', '-valid_from')


class PriceManager(models.Manager):
    def get_queryset(self) -> PriceQuerySet:
        return PriceQuerySet(model=self.model, using=self._db)
        
    def current(self):
        """ Отдает текущую цену """
        return self.get_queryset().get_current_price()

    
class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="prices")
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    valid_from = models.DateTimeField("Начало действия", default=timezone.now)
    valid_to = models.DateTimeField("Начало действия", default=datetime.max)
    
    objects = PriceManager()
    
    def __str__(self):
        return f"{self.price} руб. за {self.product}"
    
    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"
        
class Discount(models.Model):
    pass   
        