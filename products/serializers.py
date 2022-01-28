from rest_framework import serializers
from products.models import Product, ProductImage, Color
from categories.models import Category


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['title', 'articul']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class ProductSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(read_only=True, many=True)
    product_color = ProductColorSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductDetailSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()
    product_color = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'quantity', 'is_stock',
                  'category', 'product_image', 'product_color'
                  )
