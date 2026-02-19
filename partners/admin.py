from django.contrib import admin
from django.utils.html import format_html
from .models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('logo_preview', 'name', 'website_link', 'order', 'is_active', 'created_at')
    list_display_links = ('logo_preview', 'name')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'website_url')
    list_editable = ('order', 'is_active')
    readonly_fields = ('logo_preview_large', 'created_at', 'updated_at')
    list_per_page = 20
    ordering = ('order', 'name')

    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="height: 40px; width: auto; max-width: 100px; object-fit: contain; background: #f8f9fa; padding: 4px; border-radius: 6px;" />',
                obj.logo.url
            )
        return "-"
    logo_preview.short_description = "Logo"

    def logo_preview_large(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="max-height: 150px; max-width: 300px; object-fit: contain; background: #f8f9fa; padding: 16px; border-radius: 12px;" />',
                obj.logo.url
            )
        return "-"
    logo_preview_large.short_description = "Logo Preview"

    def website_link(self, obj):
        if obj.website_url:
            return format_html(
                '<a href="{}" target="_blank" style="color: #22c55e;">Visit</a>',
                obj.website_url
            )
        return "-"
    website_link.short_description = "Website"

    fieldsets = (
        ('Partner Information', {
            'fields': ('name', 'logo', 'logo_preview_large', 'website_url')
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
