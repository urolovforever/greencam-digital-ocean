from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0002_simplify_gallery_model"),
    ]

    operations = [
        # Rename image -> file
        migrations.RenameField(
            model_name="gallery",
            old_name="image",
            new_name="file",
        ),
        # Change field type from ImageField to FileField
        migrations.AlterField(
            model_name="gallery",
            name="file",
            field=models.FileField(upload_to="gallery/", verbose_name="File"),
        ),
        # Add media_type
        migrations.AddField(
            model_name="gallery",
            name="media_type",
            field=models.CharField(
                choices=[("image", "Image"), ("video", "Video")],
                default="image",
                max_length=5,
                verbose_name="Type",
            ),
        ),
        # Add caption
        migrations.AddField(
            model_name="gallery",
            name="caption",
            field=models.CharField(blank=True, max_length=255, verbose_name="Caption"),
        ),
        # Add source
        migrations.AddField(
            model_name="gallery",
            name="source",
            field=models.CharField(
                choices=[("gallery", "Gallery"), ("news", "News"), ("event", "Event")],
                default="gallery",
                max_length=10,
                verbose_name="Source",
            ),
        ),
        # Update meta
        migrations.AlterModelOptions(
            name="gallery",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Gallery Item",
                "verbose_name_plural": "Gallery Items",
            },
        ),
    ]
