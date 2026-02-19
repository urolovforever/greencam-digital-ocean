from django.db import models
from django.utils.text import slugify


class Program(models.Model):
    """Program model for campus environmental programs"""
    title = models.CharField(max_length=200, verbose_name="Program Title")
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    description = models.TextField(max_length=300, verbose_name="Short Description", help_text="Brief description for list view")
    overview = models.TextField(verbose_name="Overview", help_text="Detailed program overview")
    objectives = models.TextField(verbose_name="Objectives", help_text="Program goals and objectives")
    impact = models.TextField(verbose_name="Impact", help_text="Expected or achieved impact", blank=True)
    image = models.ImageField(upload_to='programs/', verbose_name="Program Image", blank=True, null=True)
    duration = models.CharField(max_length=100, verbose_name="Duration", blank=True, help_text="e.g., 6 months, Ongoing")
    participants = models.IntegerField(default=0, verbose_name="Number of Participants")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    is_featured = models.BooleanField(default=False, verbose_name="Featured on Homepage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Program"
        verbose_name_plural = "Programs"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
