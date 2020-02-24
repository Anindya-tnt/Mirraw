from django.contrib import admin

# Register your models here.
from .models import Artist, Product, Category, Coupon


class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]


class ProdAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['id', 'name', 'product_desc', 'artist', 'category', 'marked_price', 'discounted_price']}),
    ]


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['id', 'name']}),
    ]


class CouponAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [ 'id', 'name', 'percentage']}),
    ]


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Product, ProdAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Coupon, CouponAdmin)