from django.urls import path, include
from rest_framework import routers
from core.api import views
from .views import Productview

router = routers.DefaultRouter()
router.register(r'Product', views.Productview, 'Product')

urlpatterns = [
    path('', include(router.urls)),
]