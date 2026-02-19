# Generated migration to remove translation fields

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_description_event_description_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='event',
            name='name_uz',
        ),
        migrations.RemoveField(
            model_name='event',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='event',
            name='location_en',
        ),
        migrations.RemoveField(
            model_name='event',
            name='location_uz',
        ),
        migrations.RemoveField(
            model_name='event',
            name='location_ru',
        ),
        migrations.RemoveField(
            model_name='event',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='event',
            name='description_uz',
        ),
        migrations.RemoveField(
            model_name='event',
            name='description_ru',
        ),
    ]
