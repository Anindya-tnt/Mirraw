# Generated by Django 2.1.5 on 2020-02-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mirraw', '0007_coupon'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProdArtist',
        ),
        migrations.AddField(
            model_name='coupon',
            name='id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
