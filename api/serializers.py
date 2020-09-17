from rest_framework import serializers
from .models import Profile, SellerProfile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'address', 'address', 'profile_type', 'phone_number', 'country', 'state', 'city')


class SellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SellerProfile
        fields = ('profile', 'business_name', 'business_description', 'address', 'email', 'phone')
