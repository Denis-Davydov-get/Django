# Generated by Django 4.2.13 on 2024-06-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0003_rename_password_user_address_rename_age_user_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]
