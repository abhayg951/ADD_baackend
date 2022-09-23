"""ADD_shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from graphene_django.views import GraphQLView
# from graphene_file_upload.django import FileUploadGraphQLView
# from core.schema import schema
from core.views import Productview
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'Product', views.Productview, 'Product')
router.register(r'itemcard', views.Cardview, 'itemcard')
router.register(r'contactus', views.Contactusview, 'contact_us')

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
    # path("graphql", FileUploadGraphQLView.as_view(graphiql=True, schema=schema)),
    # path('wel/', ReactView.as_view(), name="something")
    path('api/', include(router.urls)),
]
