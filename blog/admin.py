from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ("title", "published", "publish_date")
    fields = ("title", "opening_content", "extended_content", "published")
    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.prepopulated_fields = {}
            return self.readonly_fields + ('slug',)
        return self.readonly_fields
