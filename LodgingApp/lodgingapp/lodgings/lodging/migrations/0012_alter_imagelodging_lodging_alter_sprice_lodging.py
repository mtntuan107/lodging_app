# Generated by Django 5.0.6 on 2024-05-27 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodging', '0011_alter_user_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagelodging',
            name='lodging',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_lodging', to='lodging.lodging'),
        ),
        migrations.AlterField(
            model_name='sprice',
            name='lodging',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_price', to='lodging.lodging'),
        ),
    ]
