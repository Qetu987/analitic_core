from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Heading, Category, Type, Brand, Item_model
from .serializers import HeadingListSerializer, CategoryListSerializer, \
    TypeListSerializer, BrandListSerializer, Item_modelListSerializer


class HeadingListView(APIView):
    def get(delf, request):
        headings = Heading.objects.all()
        serializer = HeadingListSerializer(headings, many=True)
        return Response(serializer.data)


class CategoryListView(APIView):
    def get(delf, request, item):
        category = Category.objects.filter(heading__id=item)
        serializer = CategoryListSerializer(category, many=True)
        return Response(serializer.data)


class TypeListView(APIView):
    def get(delf, request, item):
        type = Type.objects.filter(category__id=item)
        serializer = TypeListSerializer(type, many=True)
        return Response(serializer.data)


class BrandListView(APIView):
    def get(delf, request, item):
        brand = Brand.objects.filter(type__id=item)
        serializer = BrandListSerializer(brand, many=True)
        return Response(serializer.data)


class Item_modelListView(APIView):
    def get(delf, request, item):
        item_model = Item_model.objects.filter(brand__id=item)
        serializer = Item_modelListSerializer(item_model, many=True)
        return Response(serializer.data)