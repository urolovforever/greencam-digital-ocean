from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_remove_translation_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='video',
            field=models.FileField(blank=True, help_text='Upload MP4, WebM, or OGG video', null=True, upload_to='news/videos/', verbose_name='Video'),
        ),
    ]
