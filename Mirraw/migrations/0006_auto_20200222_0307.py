# Generated by Django 2.1.5 on 2020-02-21 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mirraw', '0005_auto_20200222_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='marked_price',
            field=models.FloatField(),
        ),
    ]
