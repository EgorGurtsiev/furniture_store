from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from tree_queries.models import TreeNode
from uuid import uuid4
from eav.decorators import register_eav


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


@register_eav()
class Product(models.Model):
    slug=models.SlugField(max_length=255, unique=True, db_index=True)
    name=models.CharField(verbose_name="Название", max_length=255, db_index=True)
    category=models.ForeignKey(Category, on_delete=models.PROTECT)
    
    def get_absolute_url(self):
        return reverse("product", kwargs={"product_slug": self.slug})
    
    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = f"{slugify(self.name)}-{uuid4().hex[:6]}"
       super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    
class ProductImage(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name="image")
    original=models.ImageField(verbose_name="Изображение", upload_to='product/original')
    thumbnail=ProcessedImageField(
        verbose_name="Миниатюра",
        upload_to='Миниатюра/thumbnail',
        help_text="200x150px",
        processors=[ResizeToFill(200, 150)],
        format='JPEG',
        options={'quality': 80},
    )
    medium=ProcessedImageField(
        verbose_name="Средний размер",
        upload_to='product/medium',
        processors=[ResizeToFill(400, 300)], 
        help_text="400x300px",
        format='JPEG',
        options={'quality': 80},
    )
    
    def __str__(self):
        return f"Изображение для {self.product.name}"
    