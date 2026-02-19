from django.db import models


class Partner(models.Model):
    """Model representing a partner organization"""
    name = models.CharField(max_length=200, verbose_name="Partner Name")
    logo = models.ImageField(upload_to='partners/', verbose_name="Partner Logo")
    website_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="Website URL")
    order = models.IntegerField(default=0, verbose_name="Display Order")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
