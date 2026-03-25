from django.contrib import admin
from django.utils.html import format_html
from .models import Program, ProgramMedia


class ProgramMediaInline(admin.TabularInline):
    model = ProgramMedia
    extra = 1
    fields = ('media_type', 'file', 'caption', 'is_cover', 'order')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'participants', 'is_active', 'is_featured', 'media_count', 'created_at')
    list_filter = ('is_active', 'is_featured', 'created_at')
    search_fields = ('title', 'description', 'overview')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_editable = ('is_active', 'is_featured')
    list_per_page = 20
    save_on_top = True
    inlines = [ProgramMediaInline]

    def media_count(self, obj):
        count = obj.media.count()
        return format_html('<span style="color: #3b82f6; font-weight: bold;">{}</span>', count)
    media_count.short_description = 'Media'

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description')
        }),
        ('Details', {
            'fields': ('overview', 'objectives', 'impact', 'duration', 'participants')
        }),
        ('Settings', {
            'fields': ('is_active', 'is_featured')
        }),
    )
