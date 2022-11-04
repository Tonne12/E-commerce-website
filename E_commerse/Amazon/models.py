from django.db import models

# Create your models here.
class Product(models.Model):
    color=models.CharField(max_length=100)
    brand=models.CharField(max_length=200)
    material=models.CharField(max_length=250)
    item=models.CharField(max_length=300)
    weight=models.CharField(max_length=350)

    def __str__(self):
        return self.item

