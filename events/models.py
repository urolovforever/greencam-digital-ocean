from django.db import models


class Event(models.Model):
    """Event model for managing campus events"""
    name = models.CharField(max_length=200, verbose_name="Event Name")
    date = models.DateField(verbose_name="Event Date")
    location = models.CharField(max_length=200, verbose_name="Location")
    description = models.TextField(verbose_name="Description", blank=True)
    is_featured = models.BooleanField(default=False, verbose_name="Featured on Homepage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.name


class Registration(models.Model):
    """Registration model for event attendees"""
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
        unique_together = ['event', 'email']  # Prevent duplicate registrations

    def __str__(self):
        return f"{self.full_name} - {self.event.name}"
