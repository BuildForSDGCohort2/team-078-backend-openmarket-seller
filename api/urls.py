from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'BuyerProfile', views.ProfileViewSet, basename='buyer')
router.register(r'SellerProfile', views.SellerViewSet, basename='Seller')


urlpatterns = [
    path('', include(router.urls)),
    path('api', include('rest_framework.urls', namespace='rest_framework'))
]
