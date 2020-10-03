from django.db import models
from django import forms
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
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.TextField(max_length=512, blank=True, null=True)
    profile_type = models.CharField(choices=PROFILE_TYPES, default="Buyer", max_length=6)
    country = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    city = models.CharField(max_length=225)

    def __str__(self):
        return self.user

#base model class for common fields
class WithInheritableColumn(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    is_active  = models.BooleanField(default=False)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    deleted_by = models.IntegerField(null=True)
    
    class Meta:
        abstract = True

class SellerProfile(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100, unique=True)
    business_description = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.business_name

class Category(WithInheritableColumn):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)
    parent = models.ForeignKey('Category', models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
    class Meta():
        """
        Meta class
        """
        verbose_name_plural = 'Categories'

class Product(WithInheritableColumn):
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller_profile = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
    price = models.CharField(max_length=100)
    unit = models.FloatField()
    unit_of_measurement = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Order(WithInheritableColumn):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    additional_detail = models.TextField(null=True)
    shipping_cost = models.FloatField()
    products = models.ManyToManyField(Product, through='OrderDetail')

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit = models.FloatField()

