# Generated by Django 2.0.5 on 2018-08-13 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0009_auto_20180809_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars'),
        ),
    ]
