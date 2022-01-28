from rest_framework import routers
from products import views
from django.urls import path

router = routers.DefaultRouter()
router.register(r'products', views.ProductAPIViewSet, basename='product_view')

urlpatterns = [
    path('products/', views.ProductAPIViewSet.as_view({'get': 'list'}), name='products_view')

]

urlpatterns += router.urls
