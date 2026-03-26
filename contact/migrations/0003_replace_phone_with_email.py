from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0002_remove_contact_email_contact_phone"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="phone",
        ),
        migrations.AddField(
            model_name="contact",
            name="email",
            field=models.EmailField(default="", max_length=254, verbose_name="Email Address"),
            preserve_default=False,
        ),
    ]
