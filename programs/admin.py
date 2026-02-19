from django.contrib import admin
from django.utils.html import format_html
from .models import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'duration', 'participants', 'is_active', 'is_featured', 'created_at')
    list_filter = ('is_active', 'is_featured', 'created_at')
    search_fields = ('title', 'description', 'overview')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_editable = ('is_active', 'is_featured')
    list_per_page = 20
    save_on_top = True

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 40px; width: 40px; object-fit: cover; border-radius: 8px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Image"

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Details', {
            'fields': ('overview', 'objectives', 'impact', 'duration', 'participants')
        }),
        ('Settings', {
            'fields': ('is_active', 'is_featured')
        }),
    )
