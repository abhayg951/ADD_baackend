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
    image = models.ForeignKey('mult_img',related_name = "photo",on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='items/', blank = True)
    # icon = CloudinaryField('image', null=True, blank=True)
    brand = models.CharField(max_length=150)
    item_name = models.TextField()
    original_mrp = models.DecimalField(
        max_digits=7, 
        decimal_places=2,
        null = True)
    discounted_percent = models.DecimalField(("discount  %"),
        max_digits=7,
        decimal_places=2,
        null = True)
    status = models.BooleanField()
    quantity = models.IntegerField(null = True)
    rating = models.IntegerField(null = True)
    product_details = models.TextField(null=True)
    date_created = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=150, null = True)
    
    
    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.brand

# class itemcard(models.Model):
#     # image = models.ForeignKey('pics',  on_delete=models.CASCADE)
#     pics = models.ImageField(upload_to='items/', blank = True)
#     brand = models.CharField(max_length=150)
#     original_mrp = models.DecimalField(
#         max_digits=7, 
#         decimal_places=2,
#         null = True)
#     discounted_mrp = models.DecimalField(
#         max_digits=7,
#         decimal_places=2,
#         null = True)
#     rating = models.IntegerField(null = True)

    # def __str__(self) -> str:
    #     return self.brand

# class contact_us(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(null= True)
#     phone = PhoneNumberField(region= 'IN')
#     desc = models.TextField(null=True)

'''
---------------------------for multiple images-----------------------------------'''

class mult_img(models.Model):
    brand = models.CharField(max_length=50, null=True)
    image1 = models.ImageField(upload_to='items/', blank = True)
    image2 = models.ImageField(upload_to='items/', blank = True)
    image3 = models.ImageField(upload_to='items/', blank = True)
    image4 = models.ImageField(upload_to='items/', blank = True)
    image5 = models.ImageField(upload_to='items/', blank = True)

    def __str__(self):
        return self.brand