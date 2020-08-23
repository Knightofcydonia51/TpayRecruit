from django.shortcuts import render, get_object_or_404
from .models import Product, ProductOption, Tag
from .serializers import ProductSerializer, ProductOptionSerializer, TagSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset
    
    def create(self, request):

        tag_set=[]
        tag_info=[]
        for i in request.data.get('tag_set'):
            if Tag.objects.filter(name=i.get('name')):
                tag_info.append((i.get('pk'),i.get('name')))
            else:
                tag_set.append(i)
        
        print(request.data)
        request.data['tag_set']=tag_set
  
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
        product=get_object_or_404(Product, pk=serializer.data.get("pk"))
        for i in range(len(tag_info)):
            product.tag_set.add(Tag.objects.filter(name=tag_info[i][1])[0])
            tag_set.append({ 'pk' : tag_info[i][0], 'name' : tag_info[i][1] })
            print(tag_set)
        
        print(serializer.data)
        
        serializer.data['tag_set']=tag_set
        
        return Response(serializer.data)


    def patch(self, request, pk):
        testmodel_object = self.get_object(pk)
        serializer = ProductSerializer(testmodel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)