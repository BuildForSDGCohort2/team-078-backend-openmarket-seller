from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'create/order', views.CreateOrderViewSet, basename='create_order')
router.register(r'seller/orders', views.ListSellerOrderViewSet, basename='seller_orders')
router.register(r'buyer/orders', views.ListBuyerOrderViewSet, basename='buyer_orders')