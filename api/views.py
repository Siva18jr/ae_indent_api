from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import *

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
            'Endpoint': '/outlets/create/',
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