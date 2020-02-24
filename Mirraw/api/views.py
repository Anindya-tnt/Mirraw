from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Mirraw.models import Artist, Product, Category, Coupon
from Mirraw.api.serializers import ProductSerializer, ArtistSerializer, CategorySerializer, \
    CouponSerializer

from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas


@api_view(['GET', ])
def api_detail_product_view(request, id):
    '''
    To get all details of a product, passing product id as parameter
    e.g. http://127.0.0.1:8000/api/product/1
    This is used to retrieve a JSON object containing details of product with id = 1
    '''
    try:
        print('*********************In Detail Product View API*******************')
        product = Product.objects.get(pk=id)
        print(product)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)


@api_view(['GET', ])
def api_all_products_view(request):
    '''
    To get details of all products

    e.g. http://127.0.0.1:8000/api/product

    This is used to retrieve a JSON object containing details of all products
    '''
    try:
        print('*********************In All Products View API*******************')
        products = Product.objects.all()
        #print(product)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def api_detail_category_view(request, id):
    '''
    To get all details of a category, passing category id as parameter
    e.g. http://127.0.0.1:8000/api/category/1
    This is used to retrieve a JSON object containing details of category with id = 1
    '''
    try:
        print('******************In Detail Category View API*******************')
        category = Category.objects.get(pk=id)
        print(category)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(['GET', ])
def api_detail_artist_view(request, id):
    '''
    To get all details of a artist, passing artist id as parameter
    e.g. http://127.0.0.1:8000/api/artist/1
    This is used to retrieve a JSON object containing details of artist with id = 1
    '''
    try:
        print('******************In Detail Artist View API*******************')
        artist = Artist.objects.get(pk=id)
        print(artist)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)


@api_view(['PUT', ])
def api_apply_coupon_per_criteria_view(request):
    '''

    To set discount for product which satisfy criteria in query string

    e.g. http://127.0.0.1:8000/api/coupon/product?artist=1&category=1
    with request body as
    {
	"coupon_name" : "GET25OFF"
    }

    This will set 25% off for all the products for artist id = 1 and category id = 1

    '''
    try:
        print('******Applying Coupon across products based on criteria************')
        print(request.query_params)
        print(request.data)

        category, artist = None, None

        category_id = request.query_params.get('category', None)
        if category_id is not None:
            category_id = int(category_id[0])
            category = Category.objects.get(pk=category_id)

        artist_id = request.query_params.get('artist', None)
        if artist_id is not None:
            artist_id = int(artist_id[0])
            artist = Artist.objects.get(pk=artist_id)
        print(category)
        print(artist)
        if category and not artist:
            products = Product.objects.filter(category=category)
        elif artist and not category:
            products = Product.objects.filter(artist=artist)
        else:
            products = Product.objects.filter(category=category, artist=artist)

        coupon_name = request.data['coupon_name']
        coupon = Coupon.objects.get(pk=coupon_name)
        print(coupon)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        result = dict()
        for product in products:
            print('Iterating', str(product))
            product.discounted_price = product.marked_price * (1 - coupon.percentage)
            product.save()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['PUT', ])
def api_apply_coupon_single_product_view(request, id):
    '''

    To set discount for a specific product

    e.g. http://127.0.0.1:8000/api/coupon/product/1
    with request body as
    {
	"coupon_name" : "GET25OFF"
    }

    This will set 25% off for a product which product id = 1

    '''
    try:
        print('******Applying Coupon on single product************')
        print(request.data)
        product = Product.objects.get(pk=id)

        coupon_name = request.data['coupon_name']
        coupon = Coupon.objects.get(pk=coupon_name)
        print(coupon)

    except Exception as e:
        print(e)
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        product.discounted_price = product.marked_price * (1 - coupon.percentage)
        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)


@api_view(['GET', ])
def api_all_coupon_view(request):
    '''
        To get details of all coupons
        e.g. http://127.0.0.1:8000/api/coupon
        This is used to retrieve a JSON object containing details of all coupons
    '''
    try:
        print('******************In Detail Coupon View API*******************')
        coupons = Coupon.objects.all()
        print(coupons)
    except Coupon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CouponSerializer(coupons, many=True)
        return Response(serializer.data)
