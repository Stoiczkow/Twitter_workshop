# Generated by Django 2.0.5 on 2018-08-13 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0011_auto_20180813_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='templates/twitter_app/avatars'),
        ),
    ]