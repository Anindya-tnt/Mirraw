# Mirraw
A django application which accepts API request to perform application of coupons on products based on criteria

Steps to run the project:
1.	Open command prompt in admin mode.
2.	Go to project base folder i.e. <path to project base folder>/mirraw_proj
3.	Run command to activate virtualenv:
Scripts\activate
4.	Run command to install package requirements:
pip install -r requirements.txt
5.	Run command to migrate db models
python manage.py migrate
6.	Run command to start Django server in local dev environment
python manage.py runserver
7.	Hit the following URL for getting the list of APIs supported in the Django application
http://localhost:8000/api/

Although the documentation is supported by coreapi, it is recommended to test the APIs using postman application.

8.	Hit the following URL to perform CRUD operations as deemed necessary on the existing Django models.

http://localhost:8000/admin/

If prompted, use the following:
Username: admin
Password: 11111111
Please feel free add rows to the db tables.
9.	For testing the APIs, please refer to the api documentation as aforesaid in point 7 above.

10.	For testing the features which were enlisted in the mail, following are the APIs of interest:

A.	A coupon can be applied to a specific Product – 

For applying the discount “GET25OFF” on product with ID as 1, use the following API:

Request: PUT http://localhost:8000/api/coupon/product/1 

Request body: 
{
	"coupon_name" : "GET25OFF"
}


B.	A coupon can be applied on all products of a specific Artist - 

For applying the discount “GET50OFF” on all products for artist ID as 1, use the following API endpoint:

Request: PUT http://127.0.0.1:8000/api/coupon/product?artist=1

Request body: 
{
	"coupon_name" : "GET50OFF"
}


C.	A coupon can be applied on all products of a Category - 

For applying the discount “GET25OFF” on all products of category ID as 1, use the following API endpoint:

Request: PUT http://127.0.0.1:8000/api/coupon/product?category=1

Request body: 
{
	"coupon_name" : "GET25OFF"
}

D.	A coupon can be applied on all Products in a specific Category for an Artist – 

For applying the discount “GET25OFF” on all products of category ID as 1 and artist ID as 1, use the following API endpoint:

Request: PUT http://127.0.0.1:8000/api/coupon/product?artist=1&category=1 

Request body: 
{
	"coupon_name" : "GET25OFF"
}

11.	In case of any clarification, please revert back over mail or phone. Thanks

N.B. – Tested on windows 10 with python3 all the environment settings as listed on requirements.txt
