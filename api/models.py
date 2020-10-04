from django.db import models
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()

PROFILE_TYPES = (
    ("Buyer", "Buyer"),
    ("Seller", "Seller"),
)

class Profile(models.Model):
    """
    User Profile
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, editable=False)
    address = models.TextField(max_length=512, blank=True, null=True)
    profile_type = models.CharField(choices=PROFILE_TYPES, default="Buyer", max_length=6)
    country = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    city = models.CharField(max_length=225)

    def __str__(self):
        return self.user.email

class SellerProfile(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100, unique=True)
    business_description = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.business_name

