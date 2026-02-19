# Generated migration to remove translation fields

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_add_translation_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_uz',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='news',
            name='excerpt_en',
        ),
        migrations.RemoveField(
            model_name='news',
            name='excerpt_uz',
        ),
        migrations.RemoveField(
            model_name='news',
            name='excerpt_ru',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_en',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_uz',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_ru',
        ),
    ]
