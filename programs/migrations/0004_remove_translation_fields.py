# Generated migration to remove translation fields

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0003_add_translation_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='program',
            name='title_uz',
        ),
        migrations.RemoveField(
            model_name='program',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='program',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='program',
            name='description_uz',
        ),
        migrations.RemoveField(
            model_name='program',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='program',
            name='overview_en',
        ),
        migrations.RemoveField(
            model_name='program',
            name='overview_uz',
        ),
        migrations.RemoveField(
            model_name='program',
            name='overview_ru',
        ),
        migrations.RemoveField(
            model_name='program',
            name='objectives_en',
        ),
        migrations.RemoveField(
            model_name='program',
            name='objectives_uz',
        ),
        migrations.RemoveField(
            model_name='program',
            name='objectives_ru',
        ),
        migrations.RemoveField(
            model_name='program',
            name='impact_en',
        ),
        migrations.RemoveField(
            model_name='program',
            name='impact_uz',
        ),
        migrations.RemoveField(
            model_name='program',
            name='impact_ru',
        ),
        migrations.RemoveField(
            model_name='program',
            name='duration_en',
        ),
        migrations.RemoveField(
            model_name='program',
            name='duration_uz',
        ),
        migrations.RemoveField(
            model_name='program',
            name='duration_ru',
        ),
    ]
