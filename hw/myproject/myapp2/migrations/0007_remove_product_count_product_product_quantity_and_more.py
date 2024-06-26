# Generated by Django 5.0.6 on 2024-06-27 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0006_remove_user_image_user_product_image_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='count_product',
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=5.0, max_digits=3),
        ),
    ]
