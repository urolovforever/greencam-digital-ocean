from django.db import models


class Gallery(models.Model):
    """Gallery model for storing images"""

    image = models.ImageField(upload_to='gallery/', verbose_name="Image")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
        ordering = ['-created_at']

    def __str__(self):
        return f"Image {self.id}"
