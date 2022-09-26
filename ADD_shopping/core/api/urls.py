from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.api import views
from .views import Productview

# router = routers.DefaultRouter()
router = DefaultRouter()
router.register(r'Product', views.Productview, 'Product')
# router.register(r'Product', views.Productview, 'Product')

urlpatterns = [
    path('', include(router.urls)),
]