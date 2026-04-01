from django.db import models
from core.utils import get_translated


class Event(models.Model):
    name = models.CharField(max_length=200, verbose_name="Event Name (EN)")
    name_uz = models.CharField(max_length=200, blank=True, verbose_name="Event Name (UZ)")
    date = models.DateField(verbose_name="Event Date")
    location = models.CharField(max_length=200, verbose_name="Location (EN)")
    location_uz = models.CharField(max_length=200, blank=True, verbose_name="Location (UZ)")
    description = models.TextField(verbose_name="Description (EN)", blank=True)
    description_uz = models.TextField(blank=True, verbose_name="Description (UZ)")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    is_featured = models.BooleanField(default=False, verbose_name="Featured on Homepage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']
        verbose_name = "Meeting"
        verbose_name_plural = "Meetings"

    def __str__(self):
        return self.name

    @property
    def translated_name(self):
        return get_translated(self, 'name')

    @property
    def translated_location(self):
        return get_translated(self, 'location')

    @property
    def translated_description(self):
        return get_translated(self, 'description')


class EventMedia(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='media', verbose_name="Event")
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES, verbose_name="Type")
    file = models.FileField(upload_to='events/media/', verbose_name="File")
    caption = models.CharField(max_length=255, blank=True, verbose_name="Caption")
    order = models.PositiveIntegerField(default=0, verbose_name="Order")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Event Media"
        verbose_name_plural = "Event Media"

    def __str__(self):
        return f"{self.get_media_type_display()} - {self.event.name}"


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations', verbose_name="Event")
    full_name = models.CharField(max_length=200, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Phone Number")
    note = models.TextField(verbose_name="Additional Note", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Registration"
        verbose_name_plural = "Registrations"
        unique_together = ['event', 'email']

    def __str__(self):
        return f"{self.full_name} - {self.event.name}"
