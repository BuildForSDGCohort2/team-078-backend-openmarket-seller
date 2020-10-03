from django.db import models
class Product(models.Model):
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # seller_profile = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
    price = models.CharField(max_length=100)
    unit = models.FloatField()
    unit_of_measurement = models.CharField(max_length=255)

    def __str__(self):
        # String 
        return self.name
