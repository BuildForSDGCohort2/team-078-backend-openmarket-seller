from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'address', 'address', 'profile_type', 'phone_number', 'country', 'state', 'city')