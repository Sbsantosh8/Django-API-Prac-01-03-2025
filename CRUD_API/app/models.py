from django.db import models

# Create your models here.


class Product(models.Model):
    print("form product models ....")
    name = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField(default=0)
