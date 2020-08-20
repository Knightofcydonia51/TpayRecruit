from django.shortcuts import render
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    # serializer : musics(queryset) -> json
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)