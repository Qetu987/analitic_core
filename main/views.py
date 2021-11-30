from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    Heading, 
    Category, 
    Type, 
    Brand, 
    Item_model
    )

from olx.models import Olx_items

from .serializers import (
    HeadingListSerializer, 
    CategoryListSerializer,
    TypeListSerializer, 
    BrandListSerializer,
    Item_modelListSerializer,
    OlxSetSerializer,
    )


class HeadingListView(APIView):
    def get(self, request):
        headings = Heading.objects.all()
        serializer = HeadingListSerializer(headings, many=True)
        return Response(serializer.data)


class CategoryListView(APIView):
    def get(self, request, item):
        category = Category.objects.filter(heading__id=item)
        serializer = CategoryListSerializer(category, many=True)
        return Response(serializer.data)


class TypeListView(APIView):
    def get(self, request, item):
        type = Type.objects.filter(category__id=item)
        serializer = TypeListSerializer(type, many=True)
        return Response(serializer.data)


class BrandListView(APIView):
    def get(self, request, item):
        brand = Brand.objects.filter(type__id=item)
        serializer = BrandListSerializer(brand, many=True)
        return Response(serializer.data)


class Item_modelListView(APIView):
    def get(self, request, item):
        item_model = Item_model.objects.filter(brand__id=item)
        serializer = Item_modelListSerializer(item_model, many=True)
        return Response(serializer.data)


class OlxSetView(APIView):
    def post(self, request):
        olx = OlxSetSerializer(data=request.data)
        if olx.is_valid():
            olx.save()
            return Response(status=201)
        return Response(status=400)