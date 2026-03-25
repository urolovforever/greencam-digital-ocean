from django.contrib import admin
from django.utils.html import format_html
from .models import Material, AboutContent, AboutImage


@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ('page', 'title', 'tag')
    fieldsets = (
        (None, {
            'fields': ('page', 'tag', 'title', 'content')
        }),
    )

    def has_add_permission(self, request):
        # Max 2: one for home, one for about
        if AboutContent.objects.count() >= 2:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(AboutImage)
class AboutImageAdmin(admin.ModelAdmin):
    list_display = ('preview', 'caption', 'is_featured', 'order')
    list_editable = ('is_featured', 'order')
    ordering = ('order',)

    def preview(self, obj):
        return format_html('<img src="{}" style="height:40px; width:60px; object-fit:cover; border-radius:6px;" />', obj.image.url)
    preview.short_description = 'Image'


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)
