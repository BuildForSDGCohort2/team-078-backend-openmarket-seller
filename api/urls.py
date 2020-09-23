from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'signup', views.SignUpViewSet, basename='signup')
router.register(r'login', views.LoginViewSet, basename='login')
router.register(r'logout', views.LogoutViewSet, basename='logout')
router.register(r'BuyerProfile', views.ProfileViewSet, basename='buyer')
router.register(r'SellerProfile', views.SellerViewSet, basename='Seller')
router.register(r'category', views.CategoryViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'create/order', views.CreateOrderViewSet, basename='create_order')
router.register(r'seller/orders', views.ListSellerOrderViewSet, basename='seller_orders')
router.register(r'buyer/orders', views.ListBuyerOrderViewSet, basename='buyer_orders')




urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
