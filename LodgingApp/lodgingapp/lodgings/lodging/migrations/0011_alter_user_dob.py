# Generated by Django 5.0.6 on 2024-05-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodging', '0010_lodging_description_alter_comment_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(default=None),
        ),
    ]
