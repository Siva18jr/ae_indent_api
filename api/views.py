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
            'description': 'Returns an array of outlet products'
        },
        {
            'Endpoint': '/outletproducts/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new product for outlet with data sent in post request'
        },
        {
            'Endpoint': '/outletproducts/id/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing outlet with data sent in post request'
        },
        {
            'Endpoint': '/outletproducts/id/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting outlet product'
        },
        {
            'Endpoint': '/saleproducts/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of sale products'
        },
        {
            'Endpoint': '/saleproducts/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new product for sales with data sent in post request'
        },
                {
            'Endpoint': '/saleproducts/id/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing sale with data sent in post request'
        },
        {
            'Endpoint': '/auth/',
            'method': 'GET',
            'body': {'parms': ""},
            'description': 'Check the user'
        },
        {
            'Endpoint': '/auth/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates an new account'
        },
        {
            'Endpoint': '/verify/',
            'method': 'GET',
            'body': {'body': ""},
            'description': 'Verify the email exists'
        },
        {
            'Endpoint': '/otp/',
            'method': 'GET',
            'body': {'body': ""},
            'description': 'Get the email otp sent to the user'
        },
        {
            'Endpoint': '/categories/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of categories'
        },
        {
            'Endpoint': '/remainingproducts/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of remainingproducts'
        },
        {
            'Endpoint': '/remainingproducts/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new remaining products with data sent in post request'
        },
                {
            'Endpoint': '/remainingproducts/id/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing remaining products with data sent in post request'
        }
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
    

@api_view(['PUT', 'DELETE'])
def getproduct(request, pk):

    if request.method == 'PUT':
        return updateProduct(request, pk)

    if request.method == 'DELETE':
        return deleteProduct(request, pk)
    

@api_view(['GET', 'POST'])
def getOutletProducts(request):

    if request.method == 'GET':
        return getOutletProductsList(request)

    if request.method == 'POST':
        return addOutletProduct(request)
    

@api_view(['PUT', 'DELETE'])
def getOutletproduct(request, pk):

    if request.method == 'PUT':
        return updateOutletProduct(request, pk)
    
    if request.method == 'DELETE':
        return deleteOutletProduct(request, pk)
    

@api_view(['GET', 'POST'])
def getSaleProducts(request):

    if request.method == 'GET':
        return getSaleProductsList(request)
    
    if request.method == 'POST':
        return addSaleProduct(request)
    

@api_view(['PUT'])
def getSaleproduct(request, pk):

    if request.method == 'PUT':
        return updateSaleProduct(request, pk)
    

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
    

@api_view(['GET'])
def getCategory(request):

    if request.method == 'GET':
        return getCategories(request)
    

@api_view(['GET', 'POST'])
def getRemainingProducts(request):

    if request.method == 'GET':
        return getRemainingProductsList(request)
    
    if request.method == 'POST':
        return addRemainingProduct(request)
    

@api_view(['PUT'])
def getRemainingproduct(request, pk):

    if request.method == 'PUT':
        return updateRemainingProduct(request, pk)
    

@api_view(['GET'])
def getFilteredSales(request):

    if request.method == 'GET':
        return getSalesFilter(request)
    

@api_view(['GET'])
def getOutletProductsByCategory(request):

    if request.method == 'GET':
        return getOutletProductsListByCategory(request)
    

@api_view(['GET'])
def getOutletProductsCategory(request):

    if request.method == 'GET':
        return getOutletProductsCategories(request)
    

@api_view(['GET'])
def getSalesDetail(request):

    if request.method == 'GET':
        return getSalesDetails(request)
    

@api_view(['GET'])
def salesProductDetails(request):

    if request.method == 'GET':
        return getSalesProductDetails(request)