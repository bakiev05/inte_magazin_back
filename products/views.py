from rest_framework import viewsets, generics

from products.models import Product, ProductImage, Color
from products.serializers import ProductSerializer, ProductImageSerializer, ProductColorSerializer, \
    ProductDetailSerializer


class ProductAPIViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageAPIViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductColorAPIViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ProductColorSerializer


# class ProductDetailViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

class ProductDeleteViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class