from django.contrib import admin
from core.models import Product, itemcard, contact_us
# Register your models here.

admin.site.register(Product)
admin.site.register(itemcard)
admin.site.register(contact_us)