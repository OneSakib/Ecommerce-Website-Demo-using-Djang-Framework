# Generated by Django 3.2.4 on 2021-07-18 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210708_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=50)),
                ('c_email', models.CharField(max_length=100)),
                ('c_phone', models.CharField(max_length=50)),
                ('c_desc', models.CharField(max_length=1000)),
            ],
        ),
    ]
