from django.db import models

# Create your models here.

# Product model
class Products(models.Model):
    name = models.CharField(max_length=225)
    sku = models.CharField(max_length=225)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        indexes = [
            models.Index(fields=[ 'sku']),
            
        ]

    def __str__(self):
        return '%s' % self.product_name
   