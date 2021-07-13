from django.db import models

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_alert = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField( null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.product_name
   