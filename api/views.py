import json
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions, status

from .serializers import ProfileSerializer, SellerProfileSerializer
from .models import SellerProfile, Profile

class CreateUpdateModelViewSet(
    mixins.CreateModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet
):
    pass

class ProfileViewSet(CreateUpdateModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class BuyerProfileViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(profile_type='Buyer')

class SellerProfileViewSet(viewsets.ModelViewSet):
    queryset = SellerProfile.objects.all()
    serializer_class = SellerProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
