# Generated by Django 5.0.6 on 2024-06-15 05:28

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodging', '0018_alter_owner_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='lodging',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lodging',
            name='price',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='owner',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
    ]
