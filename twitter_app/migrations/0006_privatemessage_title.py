# Generated by Django 2.0.5 on 2018-08-09 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0005_remove_privatemessage_received_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatemessage',
            name='title',
            field=models.CharField(max_length=140, null=True),
        ),
    ]