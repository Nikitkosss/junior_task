from django.contrib import admin
from users.models import UserLectures, UserProducts


@admin.register(UserProducts)
class UserProductsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
    )
    list_filter = ('user', 'product',)
    search_fields = ('user', 'product',)


@admin.register(UserLectures)
class UserLecturesAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'lectures',
        'watched_time',
        'status',
        'last_time_watched',
    )
    list_filter = ('user', 'lectures', 'status', 'last_time_watched',)
    search_fields = ('user', 'lectures', 'status',)
