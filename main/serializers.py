from rest_framework import serializers
from .models import Heading, Category, Type, Brand, Item_model


class HeadingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Heading
        fields = ('id', 'title', 'name_pattern')


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title', 'name_pattern')


class TypeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ('id', 'title', 'name_pattern')


class BrandListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('id', 'title', 'name_pattern')


class Item_modelListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item_model
        fields = ('id', 'title', 'name_pattern')