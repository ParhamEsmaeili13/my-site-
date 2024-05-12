from django.contrib import admin
from .models import Article


@admin.register(Article)
class ImageAdmin(admin.ModelAdmin):

    list_display = ('title', 'body', 'creat_at')
    prepopulated_fields = {'slug': ('title',)}

