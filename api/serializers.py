from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Profile, SellerProfile, Category, Order, Product


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'address', 'profile_type', 'phone_number', 'country', 'state', 'city')
        extra_kwargs = {
            'password': {'write_only': True}
        }

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = ['profile', 'business_name', 'business_description', 'address', 'email', 'phone']

class SignUpSerializer(ProfileSerializer):
    def create(self, validated_data):
        password = validated_data.get('password')
        validated_data.pop('password')
        return Profile.objects.create(
            password=make_password(password),
            **validated_data
        )

    class Meta(ProfileSerializer.Meta):
        fields = ProfileSerializer.Meta.fields + ('username','password')


class LoginSerializer(SignUpSerializer):
    class Meta(SignUpSerializer.Meta):
        read_only_fields = [
            'first_name', 'last_name', 'email', 'address', 
            'profile_type', 'phone_number', 'country', 'state', 'city'
        ]
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
