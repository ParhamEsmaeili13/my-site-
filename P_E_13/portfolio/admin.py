from django.contrib import admin
from .models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'creat_at')
    prepopulated_fields = {'slug': ('name',)}

