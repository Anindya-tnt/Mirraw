# Generated by Django 2.1.5 on 2020-02-21 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mirraw', '0003_auto_20200221_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]