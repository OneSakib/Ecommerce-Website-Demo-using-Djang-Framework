# Generated by Django 3.2.4 on 2021-07-08 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210703_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_date',
            new_name='p_date',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_desc',
            new_name='p_desc',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='p_name',
        ),
    ]