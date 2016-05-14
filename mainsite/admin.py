from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    exclude = ("slug",)
    # prepopulated_fields = {'slug': ('title',)}

