from django.db import models
from django.contrib.auth import get_user_model
from api.models import Profile, SellerProfile

User = get_user_model()

#base model class for common fields
class WithInheritableColumn(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    is_active  = models.BooleanField(default=False)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    deleted_by = models.IntegerField(null=True)
    
    class Meta:
        abstract = True

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    seller_profile = models.ForeignKey(SellerProfile, on_delete=models.CASCADE, null=True)
    price = models.CharField(max_length=100)
    unit = models.FloatField()
    unit_of_measurement = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Order(WithInheritableColumn):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    additional_detail = models.TextField(null=True)
    shipping_cost = models.FloatField()
    products = models.ManyToManyField(Product, through='OrderDetail')

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit = models.FloatField()
        
