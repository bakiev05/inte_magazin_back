from django.db import models
from categories.models import Category


class Product(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True
    )
    slug = models.SlugField(
        blank=True, unique=True
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество:'
    )
    is_stock = models.BooleanField(
        default=True,
        db_index=True
    )
    category = models.ForeignKey(
        Category,
        related_name='category_product',
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    def __str__(self):
        return f"{self.title}--{self.id}--{self.category.title}"


class Color(models.Model):
    articul = models.PositiveIntegerField(
        unique=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='product_color'
    )

    def __str__(self):
        return f"{self.title}--{self.articul}"


class ProductImage(models.Model):
    image = models.ImageField(
        upload_to='product',
        verbose_name='Картинки',
        blank=True, null=True
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='product_image'
    )

    def __str__(self):
        return f"{self.product.title} -- {self.product.id}"


