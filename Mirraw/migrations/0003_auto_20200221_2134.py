# Generated by Django 2.1.5 on 2020-02-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mirraw', '0002_auto_20200221_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.IntegerField(null=True),
        ),
    ]