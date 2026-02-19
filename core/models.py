from django.db import models


class Material(models.Model):
    """Downloadable materials"""
    name = models.CharField(max_length=200, verbose_name="Name", default="")
    file = models.FileField(upload_to='materials/', verbose_name="File")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Material"
        verbose_name_plural = "Materials"

    def __str__(self):
        return self.name
