from msilib.schema import Icon
from django.db import models
from django.db.models import Model
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Product(models.Model):
    # image = models.ImageField(upload_to='items/', blank = True)
    image = CloudinaryField('image')
    # icon = CloudinaryField('image', null=True, blank=True)
    brand = models.CharField(max_length=150)
    item = models.TextField()
    mrp = models.DecimalField(
        max_digits=7, 
        decimal_places=2,
        null = True)
    discount = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null = True)
    status = models.BooleanField()
    product_details = models.TextField(null=True)
    style_note = models.TextField(null=True)
    date_created = models.DateField(auto_now_add=True)
    slug = models.TextField(null=True)
    
    
    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.brand
