from django.urls import path

from Mirraw.api.views import api_detail_product_view, api_detail_artist_view, api_apply_coupon_per_criteria_view, \
    api_apply_coupon_single_product_view, api_detail_category_view, api_all_coupon_view, api_all_products_view

from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls


schema_view = get_swagger_view(title='Mirraw')


urlpatterns = [
    #path('', schema_view),
    path('', include_docs_urls(title='Mirraw API')),
    path('product/', api_all_products_view),
    path('product/<id>/', api_detail_product_view),
    path('artist/<id>/', api_detail_artist_view),
    path('category/<id>/', api_detail_category_view),
    path('coupon/product/<id>', api_apply_coupon_single_product_view),
    path('coupon/product', api_apply_coupon_per_criteria_view),
    path('coupon/', api_all_coupon_view)
]
