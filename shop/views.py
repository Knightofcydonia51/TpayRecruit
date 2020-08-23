from django.shortcuts import render
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
        print("Post===========")


        serializer = ProductSerializer(data=request.data)
        print(serializer)
        
        
        if serializer.is_valid(raise_exception=True):
            print("데이터================",serializer)
            serializer.save()
       
        return Response(serializer.data)

        # product = get_object_or_404(Product, pk=pk)

        # if store.like_users.filter(pk=user).exists():
        #     store.like_users.remove(user)
        # else:
        #     store.like_users.add(user)

        # serializer = serializers.LikeSerializer(instance=store)

        # return Response({
        #     'result': serializer.data,
        #     'status': status.HTTP_200_OK,
        # })