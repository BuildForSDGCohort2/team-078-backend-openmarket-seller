import json
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Profile, SellerProfile, Category, Order, Product


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'address', 'profile_type', 'phone_number', 'country', 'state', 'city')


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = ['profile', 'business_name', 'business_description', 'address', 'email', 'phone']

class SignUpSerializer(ProfileSerializer):
    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        return Profile.objects.create(
            password=make_password(validated_data.pop('password')),
            **validated_data
        )

    class Meta(ProfileSerializer.Meta):
        fields = ProfileSerializer.Meta.fields + ('password',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50,write_only=True)

    # class Meta(SignUpSerializer.Meta):
    #     read_only_fields = [
    #         'first_name', 'last_name', 'email', 'address', 
    #         'profile_type', 'phone_number', 'country', 'state', 'city'
    #     ]
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CreateProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    unit = serializers.IntegerField()

class OrderSerializer(serializers.ModelSerializer):
    product_data = CreateProductSerializer(many=True,write_only=True)

    def create(self, validated_data):
        products = validated_data.pop('product_data')
        order = Order.objects.create(**validated_data)

        for product in products:
            order.products.add(
                product['id'], 
                through_defaults={'unit':product['unit']}
            )
        return order


    class Meta:
        model = Order
        fields = '__all__'
