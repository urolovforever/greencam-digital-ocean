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

    @property
    def cover_image(self):
        """Return cover image marked in admin, or first image"""
        cover = self.media.filter(is_cover=True, media_type='image').first()
        if not cover:
            cover = self.media.filter(media_type='image').first()
        return cover.file if cover else None


class NewsMedia(models.Model):
    """Media files (images and videos) for news"""
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='media', verbose_name="News")
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES, verbose_name="Type")
    file = models.FileField(upload_to='news/media/', verbose_name="File")
    caption = models.CharField(max_length=255, blank=True, verbose_name="Caption")
    is_cover = models.BooleanField(default=False, verbose_name="Cover Image", help_text="Use as cover image on cards")
    order = models.PositiveIntegerField(default=0, verbose_name="Order")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "News Media"
        verbose_name_plural = "News Media"

    def __str__(self):
        return f"{self.get_media_type_display()} - {self.news.title}"
