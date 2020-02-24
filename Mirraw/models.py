from django.db import models


# Create your models here.
class Artist(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    product_desc = models.TextField(max_length=1000)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    marked_price = models.FloatField(null=False)
    discounted_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Coupon(models.Model):
    id = models.IntegerField(primary_key=False)
    name = models.CharField(max_length=8, primary_key=True)
    percentage = models.FloatField(default=0.0)

    def __str__(self):
        return 'Coupon {} has value of {}'.format(self.name,self.percentage)