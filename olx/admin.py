from django.contrib import admin
from .models import Olx_items, Olx_examples


@admin.register(Olx_items)
class Olx_itemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'heading', 'category', 'type', 'brand', 'item_model', 'date']
    list_display_links = ['id', 'heading', 'category', 'type', 'brand', 'item_model']
    list_search = ['id', 'heading', 'category', 'type', 'brand', 'item_model']
    list_filter = ['id']


@admin.register(Olx_examples)
class Olx_examplesAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent', 'title', 'url', 'cost']
    list_display_links = ['id', 'parent', 'title', 'url', 'cost']
    list_search = ['id', 'parent', 'title', 'url', 'cost']
    list_filter = ['id']