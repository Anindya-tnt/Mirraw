# Generated by Django 2.1.5 on 2020-02-22 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mirraw', '0006_auto_20200222_0307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('name', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('percentage', models.FloatField(default=0.0)),
            ],
        ),
    ]
