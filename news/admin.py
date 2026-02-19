from django.contrib import admin
from django.utils.html import format_html
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'category', 'is_published', 'is_featured', 'created_at')
    list_filter = ('category', 'is_published', 'is_featured', 'created_at')
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_editable = ('is_published', 'is_featured')
    list_per_page = 20
    save_on_top = True

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 40px; width: 40px; object-fit: cover; border-radius: 8px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Image"

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category')
        }),
        ('Content', {
            'fields': ('image', 'excerpt', 'content')
        }),
        ('Settings', {
            'fields': ('is_published', 'is_featured')
        }),
    )
