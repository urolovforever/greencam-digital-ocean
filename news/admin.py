from django.contrib import admin
from django.utils.html import format_html
from .models import News, NewsMedia


class NewsMediaInline(admin.TabularInline):
    model = NewsMedia
    extra = 1
    fields = ('media_type', 'file', 'caption', 'is_cover', 'order')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'is_featured', 'media_count', 'created_at')
    list_filter = ('category', 'is_published', 'is_featured', 'created_at')
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_editable = ('is_published', 'is_featured')
    list_per_page = 20
    save_on_top = True
    inlines = [NewsMediaInline]

    def media_count(self, obj):
        count = obj.media.count()
        return format_html('<span style="color: #3b82f6; font-weight: bold;">{}</span>', count)
    media_count.short_description = 'Media'

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category')
        }),
        ('Content', {
            'fields': ('excerpt', 'content')
        }),
        ('Settings', {
            'fields': ('is_published', 'is_featured')
        }),
    )
