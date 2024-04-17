from django.contrib import admin
from .models import UserContact


@admin.register(UserContact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'timestamp')
    list_filter = ('timestamp', )
    search_fields = ('name', 'subject')
