from rest_framework import serializers
from .models import Product, ProductOption, Tag
from drf_writable_nested.serializers import WritableNestedModelSerializer


class ProductOptionSerializer(serializers.ModelSerializer):

    # product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductOption
        fields = ['pk', 'name', 'price']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['pk', 'name']


class ProductSerializer(WritableNestedModelSerializer):
    


    option_set = ProductOptionSerializer(many=True)
    tag_set = TagSerializer(many=True)
    
    class Meta:
        model = Product
        fields = ['pk', 'name','option_set','tag_set']

