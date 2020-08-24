from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Product, ProductOption, Tag
from .serializers import ProductSerializer, ProductOptionSerializer, TagSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset
    
    def create(self, request):
        data=tag_validator(self, request)
        return Response(data)

    def partial_update(self, request, pk):
        data=tag_validator(self, request, pk)
        return Response(data)


def tag_validator(self, request, *args):

    tag_set=[]
    tag_info=[]
    for i in request.data.get('tag_set'):
        if Tag.objects.filter(name=i.get('name')):
            tag_info.append((i.get('pk'),i.get('name')))
        else:
            tag_set.append(i)

    request.data['tag_set']=tag_set
    
    if args: # patch
        product=get_object_or_404(Product, pk=args[0])
        serializer = ProductSerializer(product, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
            print(serializer._data)

    else: # post
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            product=get_object_or_404(Product, pk=serializer.data.get("pk"))

    while tag_info:
        pk,name = tag_info.pop()
        product.tag_set.add(Tag.objects.filter(name=name)[0])
        serializer._data['tag_set'].insert(0,{ 'pk' : pk, 'name' : name })

    return serializer._data