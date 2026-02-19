from django.db import models
from django.utils.text import slugify


class News(models.Model):
    """News model for campus news and updates"""
    CATEGORY_CHOICES = [
        ('environment', 'Environment'),
        ('community', 'Community'),
        ('achievement', 'Achievement'),
        ('research', 'Research'),
        ('event', 'Event'),
    ]

    title = models.CharField(max_length=200, verbose_name="Title")
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    excerpt = models.TextField(max_length=300, verbose_name="Excerpt", help_text="Short description for list view")
    content = models.TextField(verbose_name="Content", help_text="Full article content for detail view")
    image = models.ImageField(upload_to='news/', verbose_name="Image", blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='environment', verbose_name="Category")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name="Published")
    is_featured = models.BooleanField(default=False, verbose_name="Featured on Homepage")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
