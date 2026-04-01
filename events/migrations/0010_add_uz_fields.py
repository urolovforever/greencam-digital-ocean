from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_event_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='name_uz',
            field=models.CharField(blank=True, max_length=200, verbose_name='Event Name (UZ)'),
        ),
        migrations.AddField(
            model_name='event',
            name='location_uz',
            field=models.CharField(blank=True, max_length=200, verbose_name='Location (UZ)'),
        ),
        migrations.AddField(
            model_name='event',
            name='description_uz',
            field=models.TextField(blank=True, verbose_name='Description (UZ)'),
        ),
    ]
