# Generated migration to remove translation fields

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='name_uz',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='name_ru',
        ),
    ]
