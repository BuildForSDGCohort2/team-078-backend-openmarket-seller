import json
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework import mixins
from .serializers import (
    ProfileSerializer, SellerSerializer, CategorySerializer, 
    ProductSerializer, OrderSerializer, LoginSerializer, 
    SignUpSerializer
)
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import (
    SellerProfile, Profile, Category, Order, Product
)


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
   
    def get_queryset(self):
        qs = Profile.objects.all()
        return qs

    def perform_create(self, request, *args, **kwargs):
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    def perform_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProfileSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        


class SellerViewSet(viewsets.ModelViewSet):
    serializer_class = SellerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = SellerProfile.objects
        return qs


    def perform_create(self, request, *args, **kwargs):
        serializer = SellerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SellerSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

class CreateModelViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    pass

class SignUpViewSet(CreateModelViewSet):
    serializer_class = SignUpSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            data = {'token':token.key, **serializer.data}
            return Response(data, status.HTTP_200_OK)
        return Response(
            {'error':serializer.errors}
        )

class LoginViewSet(CreateModelViewSet):
    serializer_class = LoginSerializer

    def create(self, request):
        user = authenticate(
            email=request.data['email'], 
            password=request.data['password']
        )

        if user is not None:
            login(request, user)
            serialized = self.serializer_class(user)
            token, _ = Token.objects.get_or_create(user=user)
            data = {'token':token.key, **serialized.data}
            return Response(data, status.HTTP_200_OK)
        else:
            return Response({
               'error': 'Invalid email/password combination.'
                }, status=status.HTTP_401_UNAUTHORIZED
            )

class LogoutViewSet(CreateModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

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
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        orders = Order.objects.filter(
            profile_id=request.query_params.get('buyer_id')
        )
        serialized = OrderSerializer(orders,many=True)
        return Response(serialized.data,status.HTTP_200_OK)

class ListSellerOrderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(
            products__seller_profile_id=self.request.query_params.get('seller_id')
        )






 