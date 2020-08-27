from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProfileSerializer
from .models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('first_name')
    serializer_class = ProfileSerializer