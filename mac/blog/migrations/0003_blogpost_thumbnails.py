# Generated by Django 3.2.4 on 2021-07-30 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blogpost_thumbnails'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='thumbnails',
            field=models.ImageField(default='', upload_to='blog/images'),
        ),
    ]