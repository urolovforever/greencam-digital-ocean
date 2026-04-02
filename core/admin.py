from django.contrib import admin
from django.utils.html import format_html
from .models import HeroBG


@admin.register(HeroBG)
class HeroBGAdmin(admin.ModelAdmin):
    list_display = ('preview', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    fields = ('image', 'is_active', 'order')

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px; width:90px; object-fit:cover; border-radius:8px;" />', obj.image.url)
        return "-"
    preview.short_description = 'Image'
