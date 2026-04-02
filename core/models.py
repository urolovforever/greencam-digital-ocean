from django.db import models


class AboutContent(models.Model):
    """Editable content for the About sections"""
    PAGE_CHOICES = [
        ('home', 'Home Page'),
        ('about', 'About Page'),
    ]
    page = models.CharField(max_length=5, choices=PAGE_CHOICES, unique=True, default='home', verbose_name="Page")
    tag = models.CharField(max_length=100, verbose_name="Section Tag")
    title = models.CharField(max_length=300, verbose_name="Title")
    content = models.TextField(verbose_name="Content", help_text="Full about text. Use paragraphs for line breaks.")

    class Meta:
        verbose_name = "About Content"
        verbose_name_plural = "About Content"

    def __str__(self):
        return f"{self.get_page_display()} — {self.title}"


class AboutImage(models.Model):
    """Images for the About page carousel"""
    image = models.ImageField(upload_to='about/', verbose_name="Image")
    caption = models.CharField(max_length=255, blank=True, verbose_name="Caption")
    is_featured = models.BooleanField(default=False, verbose_name="Show on Homepage", help_text="Display this image in the About section on homepage")
    order = models.PositiveIntegerField(default=0, verbose_name="Order")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "About Image"
        verbose_name_plural = "About Images"

    def __str__(self):
        return self.caption or f"About Image #{self.pk}"


class HeroBG(models.Model):
    """Hero background images for homepage slideshow"""
    image = models.ImageField(upload_to='hero/', verbose_name="Image")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    order = models.PositiveIntegerField(default=0, verbose_name="Order")

    class Meta:
        ordering = ['order']
        verbose_name = "Hero Background"
        verbose_name_plural = "Hero Backgrounds"

    def __str__(self):
        return f"Hero BG #{self.pk}"


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
