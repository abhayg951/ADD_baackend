from core.models import Product
from .serializer import ProductSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_400_BAD_REQUEST


class Productlist(APIView):
    """
    All products are listed here.
    """
    def get(self, request, *args, **kwargs):
        products= Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        id = request.data.get('slug', None)
        if id is None:
            return Response({"message": "Invalid data"}, status=HTTP_400_BAD_REQUEST)
        # if id.is_valid():
        #     id.save()
        #     return Response(id.data, status=status.HTTP_201_CREATED)
        # return Response(id.errors, status=status.HTTP_400_BAD_REQUEST)