from rest_framework import serializers
from .models import Heading, Category, Type, Brand, Item_model
from olx.models import Olx_items, Olx_examples


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


class OlxSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Olx_items
        fields = '__all__'



class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Olx_examples
        fields = ('title', 'url', 'cost')


class OlxResultSerializer(serializers.ModelSerializer):
    childrens = ChildrenSerializer(many=True)
    heading = serializers.SlugRelatedField(slug_field="title", read_only=True)
    category = serializers.SlugRelatedField(slug_field="title", read_only=True)
    type = serializers.SlugRelatedField(slug_field="title", read_only=True)
    brand = serializers.SlugRelatedField(slug_field="title", read_only=True)
    item_model = serializers.SlugRelatedField(slug_field="title", read_only=True)
    class Meta:
        model = Olx_items
        fields = ('id', 'heading', 'category', 'type', 'brand', 'item_model', "total", "date", "childrens")