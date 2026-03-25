from django.contrib import admin
from django.utils.html import format_html
from .models import Event, EventMedia


class EventMediaInline(admin.TabularInline):
    model = EventMedia
    extra = 1
    fields = ('media_type', 'file', 'caption', 'order')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'is_active', 'is_featured', 'media_count', 'created_at')
    list_filter = ('is_active', 'date', 'is_featured', 'created_at')
    search_fields = ('name', 'location', 'description')
    date_hierarchy = 'date'
    ordering = ('-date',)
    list_editable = ('is_active', 'is_featured')
    list_per_page = 20
    save_on_top = True
    inlines = [EventMediaInline]

    def media_count(self, obj):
        count = obj.media.count()
        return format_html('<span style="color: #3b82f6; font-weight: bold;">{}</span>', count)
    media_count.short_description = 'Media'

    fieldsets = (
        ('Event Information', {
            'fields': ('name', 'date', 'location')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Settings', {
            'fields': ('is_active', 'is_featured')
        }),
    )
