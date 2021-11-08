from django.contrib import admin
from .models import Heading, Category, Brand, Item_model


@admin.register(Heading)
class HeadingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'name_pattern']
    list_display_links = ['id', 'title', 'name_pattern']
    list_search = ['id', 'title', 'name_pattern']
    list_filter = ['id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'heading', 'name_pattern']
    list_display_links = ['id', 'title', 'heading', 'name_pattern']
    list_search = ['id', 'title', 'heading', 'name_pattern']
    list_filter = ['id']
    

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'name_pattern']
    list_display_links = ['id', 'title', 'category', 'name_pattern']
    list_search = ['id', 'title', 'category', 'name_pattern']
    list_filter = ['id']


@admin.register(Item_model)
class Item_modelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'brand', 'name_pattern']
    list_display_links = ['id', 'title', 'brand', 'name_pattern']
    list_search = ['id', 'title', 'brand', 'name_pattern']
    list_filter = ['id']

