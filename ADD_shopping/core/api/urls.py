from django.urls import path, include
from rest_framework import routers
from core.api import views
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import product_list

# router = routers.DefaultRouter()
# router = routers.DefaultRouter()
# router.register(r'Product', views.Productlist.as_view, 'Product')
# router.register(r'Product', views.Productview, 'Product')

urlpatterns = [
    # path('', include(router.urls)),
    # path('', views.Productlist, 'Product'),
    path('products/', views.Productlist.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)