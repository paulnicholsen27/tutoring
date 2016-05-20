from django.contrib import admin

from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}
    list_display =("title", "published", "publish_date")