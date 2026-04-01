from django.contrib import admin
from .models import ResultCategory, ResultSubCategory, ResultFile


@admin.register(ResultCategory)
class ResultCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    fields = ('name', 'name_uz', 'order')


@admin.register(ResultSubCategory)
class ResultSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    fields = ('name', 'name_uz', 'order')


@admin.register(ResultFile)
class ResultFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'order')
    list_filter = ('category', 'subcategory')
    fields = ('category', 'subcategory', 'name', 'name_uz', 'file', 'order')
