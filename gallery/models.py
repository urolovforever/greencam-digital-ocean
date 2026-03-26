from django.db import models


class Gallery(models.Model):
    """Gallery model for storing images and videos"""
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    SOURCE_CHOICES = [
        ('gallery', 'Gallery'),
        ('news', 'News'),
        ('event', 'Event'),
    ]

    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES, default='image', verbose_name="Type")
    file = models.FileField(upload_to='gallery/', verbose_name="File")
    caption = models.CharField(max_length=255, blank=True, verbose_name="Caption")
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES, default='gallery', verbose_name="Source")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Gallery Item"
        verbose_name_plural = "Gallery Items"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_media_type_display()} {self.id}"
