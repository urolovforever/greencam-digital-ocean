from django.contrib import admin
from django.utils.html import format_html
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'subject', 'status_badge', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'phone', 'subject', 'message')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_per_page = 30
    list_editable = []
    actions = ['mark_as_read', 'mark_as_replied']

    def status_badge(self, obj):
        colors = {
            'new': '#3b82f6',
            'read': '#f59e0b',
            'replied': '#22c55e',
        }
        color = colors.get(obj.status, '#6b7280')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 4px 12px; border-radius: 12px; font-size: 11px; font-weight: 600;">{}</span>',
            color, obj.get_status_display()
        )
    status_badge.short_description = 'Status'

    @admin.action(description='Mark selected as Read')
    def mark_as_read(self, request, queryset):
        queryset.update(status='read')

    @admin.action(description='Mark selected as Replied')
    def mark_as_replied(self, request, queryset):
        queryset.update(status='replied')

    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'phone', 'subject')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return False
