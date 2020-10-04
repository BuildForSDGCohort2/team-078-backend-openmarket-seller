from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'profile/seller', views.SellerProfileViewSet)
router.register(r'profile/buyer', views.BuyerProfileViewSet, basename='buyer')
router.register(r'profile', views.ProfileViewSet, basename='profile')
