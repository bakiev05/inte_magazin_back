from django.contrib import admin
from categories.models import Category
from products.models import Product, ProductImage, Color

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Product)
admin.site.register(ProductImage)