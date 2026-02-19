from django.contrib import admin
from django.utils.html import format_html
from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'created_at')
    list_display_links = ('id', 'image_preview')
    readonly_fields = ('image_preview_large', 'created_at')
    list_per_page = 24
    ordering = ('-created_at',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height: 60px; width: 80px; object-fit: cover; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);" />',
                obj.image.url
            )
        return "-"
    image_preview.short_description = "Preview"

    def image_preview_large(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 400px; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);" />',
                obj.image.url
            )
        return "-"
    image_preview_large.short_description = "Image Preview"

    fieldsets = (
        ('Image', {
            'fields': ('image', 'image_preview_large')
        }),
        ('Info', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
