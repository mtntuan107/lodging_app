# Generated by Django 5.0.6 on 2024-06-19 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodging', '0020_remove_lodging_e_price_remove_lodging_w_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(default='2000-10-10'),
        ),
    ]
