from django.db import models
from core.utils import get_translated


class ResultCategory(models.Model):
    """WP categories - WP1, WP2, etc."""
    name = models.CharField(max_length=300, verbose_name="Name (EN)")
    name_uz = models.CharField(max_length=300, blank=True, verbose_name="Name (UZ)")
    order = models.PositiveIntegerField(default=0, verbose_name="Order")

    class Meta:
        ordering = ['order']
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    @property
    def translated_name(self):
        return get_translated(self, 'name')


class ResultSubCategory(models.Model):
    """Deliverables, Results/Outcomes, Service/Product"""
    name = models.CharField(max_length=200, verbose_name="Name (EN)")
    name_uz = models.CharField(max_length=200, blank=True, verbose_name="Name (UZ)")
    order = models.PositiveIntegerField(default=0, verbose_name="Order")

    class Meta:
        ordering = ['order']
        verbose_name = "Sub-Category"
        verbose_name_plural = "Sub-Categories"

    def __str__(self):
        return self.name

    @property
    def translated_name(self):
        return get_translated(self, 'name')


class ResultFile(models.Model):
    """Uploaded file with category + subcategory"""
    category = models.ForeignKey(ResultCategory, on_delete=models.CASCADE, related_name='files', verbose_name="Category")
    subcategory = models.ForeignKey(ResultSubCategory, on_delete=models.CASCADE, related_name='files', verbose_name="Sub-Category")
    name = models.CharField(max_length=500, verbose_name="File Name (EN)")
    name_uz = models.CharField(max_length=500, blank=True, verbose_name="File Name (UZ)")
    file = models.FileField(upload_to='results/', verbose_name="File")
    order = models.PositiveIntegerField(default=0, verbose_name="Order")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "Result File"
        verbose_name_plural = "Result Files"

    def __str__(self):
        return self.name

    @property
    def translated_name(self):
        return get_translated(self, 'name')
