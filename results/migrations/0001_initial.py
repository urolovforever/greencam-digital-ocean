from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Result Title')),
                ('wp_reference', models.CharField(blank=True, help_text='e.g., WP1, WP2', max_length=50, verbose_name='Work Package Reference')),
                ('description', models.TextField(verbose_name='Description')),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('in_progress', 'In Progress'), ('planned', 'Planned')], default='planned', max_length=15, verbose_name='Status')),
                ('file', models.FileField(blank=True, null=True, upload_to='results/', verbose_name='Downloadable File')),
                ('pub_date', models.DateField(blank=True, null=True, verbose_name='Publication Date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Result',
                'verbose_name_plural': 'Results',
                'ordering': ['wp_reference', '-created_at'],
            },
        ),
    ]
