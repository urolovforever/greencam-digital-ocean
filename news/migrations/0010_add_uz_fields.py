from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_newsmedia_is_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='title_uz',
            field=models.CharField(blank=True, max_length=200, verbose_name='Title (UZ)'),
        ),
        migrations.AddField(
            model_name='news',
            name='excerpt_uz',
            field=models.TextField(blank=True, max_length=300, verbose_name='Excerpt (UZ)'),
        ),
        migrations.AddField(
            model_name='news',
            name='content_uz',
            field=models.TextField(blank=True, verbose_name='Content (UZ)'),
        ),
    ]
