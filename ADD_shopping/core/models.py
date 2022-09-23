from django.db import models
from django.db.models import Model
# import cloudinary
# from cloudinary.models import CloudinaryField

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='items/', blank = True)
    # image = CloudinaryField('image')
    # icon = CloudinaryField('image', null=True, blank=True)
    brand = models.CharField(max_length=150)
    item = models.TextField()
    mrp = models.DecimalField(
        max_digits=7, 
        decimal_places=2,
        null = True)
    discount_Percentage = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null = True)
    status = models.BooleanField()
    rating = models.IntegerField(null = True)
    product_details = models.TextField(null=True)
    date_created = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=150, null = True)
    
    
    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.brand

class itemcard(models.Model):
    image = models.ImageField(upload_to='items/', blank = True)
    brand = models.CharField(max_length=150)
    mrp = models.DecimalField(
        max_digits=7, 
        decimal_places=2,
        null = True)

class contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null= True)
