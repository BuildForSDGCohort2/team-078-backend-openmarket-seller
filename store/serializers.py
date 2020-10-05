from rest_framework import serializers
from .models import Product, Category, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id','category','seller_profile','name', 'description', 'price', 'unit', 'unit_of_measurement')

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