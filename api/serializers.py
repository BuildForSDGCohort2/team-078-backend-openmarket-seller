from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile, SellerProfile, Category, Order, Product

   
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

    class Meta:
        model = Profile
        fields = ('user','address', 'profile_type','country', 'state', 'city')

class SellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = ['id','profile', 'business_name', 'business_description', 'address', 'email', 'phone']

