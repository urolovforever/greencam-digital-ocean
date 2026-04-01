from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultWP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wp_number', models.PositiveIntegerField(unique=True, verbose_name='WP Number')),
                ('title', models.CharField(max_length=300, verbose_name='Title (EN)')),
                ('title_uz', models.CharField(blank=True, max_length=300, verbose_name='Title (UZ)')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Result Work Package',
                'verbose_name_plural': 'Result Work Packages',
                'ordering': ['order', 'wp_number'],
            },
        ),
        migrations.CreateModel(
            name='ResultItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('deliverable', 'Deliverable'), ('outcome', 'Result/Outcome'), ('service', 'Service/Product')], max_length=20, verbose_name='Category')),
                ('text', models.CharField(max_length=500, verbose_name='Text (EN)')),
                ('text_uz', models.CharField(blank=True, max_length=500, verbose_name='Text (UZ)')),
                ('file', models.FileField(blank=True, null=True, upload_to='results/', verbose_name='Downloadable File')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
                ('wp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='results.resultwp', verbose_name='Work Package')),
            ],
            options={
                'verbose_name': 'Result Item',
                'verbose_name_plural': 'Result Items',
                'ordering': ['category', 'order'],
            },
        ),
    ]
