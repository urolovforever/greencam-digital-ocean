from django.contrib import admin
from django.utils.html import format_html
from .models import Event, Registration


class RegistrationInline(admin.TabularInline):
    model = Registration
    extra = 0
    readonly_fields = ('full_name', 'email', 'phone', 'note', 'created_at')
    can_delete = True

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'is_featured', 'registration_count', 'created_at')
    list_filter = ('date', 'is_featured', 'created_at')
    search_fields = ('name', 'location', 'description')
    date_hierarchy = 'date'
    ordering = ('-date',)
    list_editable = ('is_featured',)
    list_per_page = 20
    save_on_top = True
    inlines = [RegistrationInline]

    def registration_count(self, obj):
        count = obj.registrations.count()
        return format_html('<span style="color: #22c55e; font-weight: bold;">{}</span>', count)
    registration_count.short_description = 'Registrations'

    fieldsets = (
        ('Event Information', {
            'fields': ('name', 'date', 'location')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Settings', {
            'fields': ('is_featured',)
        }),
    )


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'event', 'created_at')
    list_filter = ('event', 'created_at')
    search_fields = ('full_name', 'email', 'phone', 'event__name')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    list_per_page = 30
    list_select_related = ('event',)

    fieldsets = (
        ('Event', {
            'fields': ('event',)
        }),
        ('Registrant Details', {
            'fields': ('full_name', 'email', 'phone', 'note')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return False
