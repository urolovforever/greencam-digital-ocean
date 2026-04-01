from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_resultwp_resultitem'),
    ]

    operations = [
        migrations.DeleteModel(name='ResultItem'),
        migrations.DeleteModel(name='Result'),
        migrations.CreateModel(
            name='ResultSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name (EN)')),
                ('name_uz', models.CharField(blank=True, max_length=200, verbose_name='Name (UZ)')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
                ('wp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='results.resultwp', verbose_name='Work Package')),
            ],
            options={
                'verbose_name': 'Sub-Category',
                'verbose_name_plural': 'Sub-Categories',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ResultFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Name (EN)')),
                ('name_uz', models.CharField(blank=True, max_length=500, verbose_name='Name (UZ)')),
                ('file', models.FileField(upload_to='results/', verbose_name='File')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='results.resultsubcategory', verbose_name='Sub-Category')),
            ],
            options={
                'verbose_name': 'Result File',
                'verbose_name_plural': 'Result Files',
                'ordering': ['order', 'created_at'],
            },
        ),
    ]
