from django.contrib import admin
from .models import Olx_items


@admin.register(Olx_items)
class Olx_itemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'cost', 'url', 'date']
    list_display_links = ['id', 'title', 'url']
    list_search = ['id', 'title', 'cost']
    list_filter = ['id']