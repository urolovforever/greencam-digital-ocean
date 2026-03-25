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

    @property
    def cover_image(self):
        """Return cover image marked in admin, or first image"""
        cover = self.media.filter(is_cover=True, media_type='image').first()
        if not cover:
            cover = self.media.filter(media_type='image').first()
        return cover.file if cover else None


class ProgramMedia(models.Model):
    """Media files (images and videos) for programs"""
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='media', verbose_name="Program")
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES, verbose_name="Type")
    file = models.FileField(upload_to='programs/media/', verbose_name="File")
    caption = models.CharField(max_length=255, blank=True, verbose_name="Caption")
    is_cover = models.BooleanField(default=False, verbose_name="Cover Image", help_text="Use as cover image on cards")
    order = models.PositiveIntegerField(default=0, verbose_name="Order")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Program Media"
        verbose_name_plural = "Program Media"

    def __str__(self):
        return f"{self.get_media_type_display()} - {self.program.title}"
