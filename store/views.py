import json
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer
from .models import Category, Order, Product


class CreateModelViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    pass
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CreateOrderViewSet(CreateModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        data = request.data.copy()
        data['profile'] = request.user.id
        serializer = self.serializer_class(data=data)
        
        if serializer.is_valid():
            order = serializer.save()
        else: 
            return Response(serializer.errors)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ListBuyerOrderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(
            user_id=self.request.query_params.get('buyer_id')
            # user__id=request.query_params.get('buyer_id')
        )

class ListSellerOrderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        filter = {
            "id":0,
            "products__seller_profile_id":self.request.query_params.get('seller_id')
        }
        if self.request.query_params.get('seller_id'):
            filter.pop('id')
        else: filter.pop('products__seller_profile_id')
        
        return Order.objects.filter(**filter)
