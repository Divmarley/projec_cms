from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255) 
    price =models.DecimalField(decimal_places=2,max_digits=4)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()



    def __str__(self):
        return self.name