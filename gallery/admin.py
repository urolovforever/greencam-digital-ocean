from django.contrib import admin
from django.utils.html import format_html
from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'media_preview', 'media_type', 'caption', 'source', 'created_at')
    list_display_links = ('id', 'media_preview')
    list_filter = ('media_type', 'source')
    readonly_fields = ('media_preview_large', 'created_at')
    list_per_page = 24
    ordering = ('-created_at',)

    def media_preview(self, obj):
        if obj.file:
            if obj.media_type == 'video':
                return format_html(
                    '<div style="height:60px; width:80px; background:#1a1a2e; border-radius:8px; display:flex; align-items:center; justify-content:center;">'
                    '<span style="color:#fff; font-size:24px;">&#9654;</span></div>'
                )
            return format_html(
                '<img src="{}" style="height: 60px; width: 80px; object-fit: cover; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);" />',
                obj.file.url
            )
        return "-"
    media_preview.short_description = "Preview"

    def media_preview_large(self, obj):
        if obj.file:
            if obj.media_type == 'video':
                return format_html(
                    '<video controls style="max-height:400px; max-width:100%; border-radius:12px;"><source src="{}" type="video/mp4"></video>',
                    obj.file.url
                )
            return format_html(
                '<img src="{}" style="max-height: 400px; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);" />',
                obj.file.url
            )
        return "-"
    media_preview_large.short_description = "Preview"

    fieldsets = (
        ('Media', {
            'fields': ('media_type', 'file', 'caption', 'media_preview_large')
        }),
        ('Info', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
