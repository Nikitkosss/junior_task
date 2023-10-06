from django.contrib import admin
from myapp.models import Lectures, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'owner',
    )
    list_filter = ('email', 'username',)
    search_fields = ('email', 'username',)


@admin.register(Lectures)
class LecturesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'link',
        'product',
        'watchnig_time',)
    list_filter = ('product', 'watchnig_time',)
    search_fields = ('name', 'product',)
