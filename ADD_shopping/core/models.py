from distutils.text_file import TextFile
from email.policy import default
from django.db import models
from django.db.models import Model
from phonenumber_field.modelfields import PhoneNumberField
# import cloudinary
# from cloudinary.models import CloudinaryField

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('WW', 'Winter Wear'),
    ('TP', 'Top wear'),
    ('BP', 'Bottom wear'),
    ('FW', 'Foot wear'),
)

# Create your models here.
class Product(models.Model):
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, null=True)
    image = models.ImageField(upload_to='items/', blank = True)
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
    discount_Percentage = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null = True)
    rating = models.IntegerField(null = True)

class contact_us(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null= True)
    phone = PhoneNumberField(region= 'IN')
    desc = models.TextField(null=True)
