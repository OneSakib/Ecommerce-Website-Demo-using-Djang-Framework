# Generated by Django 3.2.4 on 2021-07-30 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_orders_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
