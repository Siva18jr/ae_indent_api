from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import *
from django.contrib.auth.models import User
from rest_framework import generics

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/outlets/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of outlets'
        },
        {
            'Endpoint': '/outlet/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single outlet'
        },
        {
            'Endpoint': '/outlets/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new outlet with data sent in post request'
        },
        {
            'Endpoint': '/outlets/id/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing outlet with data sent in post request'
        },
        {
            'Endpoint': '/outlets/id/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting outlet'
        },
        {
            'Endpoint': '/products/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of products'
        },
        {
            'Endpoint': '/products/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new product with data sent in post request'
        },
        {
            'Endpoint': '/products/id/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting product'
        },
        {
            'Endpoint': '/outletproducts/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of outlets'
        },
        {
            'Endpoint': '/outletproduct/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new outlet with data sent in post request'
        },
        {
            'Endpoint': '/outletproducts/id/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing outlet with data sent in post request'
        },
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
def getOutlets(request):

    if request.method == 'GET':
        return getOutletList(request)

    if request.method == 'POST':
        return createOutlet(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getOutlet(request, pk):

    if request.method == 'GET':
        return getOutletDetail(request, pk)

    if request.method == 'PUT':
        return updateOutlet(request, pk)

    if request.method == 'DELETE':
        return deleteOutlet(request, pk)
    
    
@api_view(['GET', 'POST'])
def getProducts(request):

    if request.method == 'GET':
        return getProductList(request)

    if request.method == 'POST':
        return addProduct(request)
    

@api_view(['GET', 'PUT', 'DELETE'])
def getproduct(request, pk):

    if request.method == 'PUT':
        return updateProduct(request, pk)

    if request.method == 'DELETE':
        return deleteProduct(request, pk)
    

@api_view(['GET', 'POST'])
def getOutletProducts(request):

    if request.method == 'GET':
        return getOutletProducts(request)
    
    if request.method == 'POST':
        return addOutletProduct(request)
    

@api_view(['PUT'])
def getOutletproduct(request, pk):

    if request.method == 'PUT':
        return updateOutletProduct(request, pk)
    

@api_view(['GET', 'POST'])
def getSaleProducts(request):

    if request.method == 'GET':
        return getSaleProducts(request)
    
    if request.method == 'POST':
        return addSaleProduct(request)
    

@api_view(['POST', 'GET'])
def auth(request):

    if request.method == 'GET':
        return login(request)
    
    if request.method == 'POST':
        return addUser(request)
    

@api_view(['GET'])
def verification(request):

    if request.method == 'GET':
        return verifyEmail(request)
    

@api_view(['GET'])
def otp(request):

    if request.method == 'GET':
        return sendOtp(request)