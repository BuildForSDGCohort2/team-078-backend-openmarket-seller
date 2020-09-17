from rest_framework import viewsets
from .serializers import ProfileSerializer, SellerSerializer
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import SellerProfile, Profile


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


 