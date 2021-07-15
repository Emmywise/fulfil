from django.db import models

# Create your models here.

# Product model
class Products(models.Model):
    product_name = models.CharField(max_length=225)
    product_alert = models.CharField(max_length=225)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.product_name
   