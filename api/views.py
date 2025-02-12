from rest_framework.decorators import api_view
from .utils import *

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
    

@api_view(['GET', 'POST'])
def outletPending(request):

    if request.method == 'GET':
        return getOutletPending(request)
    
    if request.method == 'POST':
        return updateOutletPending(request)
    

@api_view(['GET'])
def employees(request):

    if request.method == 'GET':
        return getEmployees(request)
    

@api_view(['GET'])
def recentEmployees(request):

    if request.method == 'GET':
        return getRecentEmployees(request)
    

@api_view(['PUT', 'DELETE'])
def employee(request, pk):

    if request.method == 'PUT':
        return updateEmployeeData(request, pk)
    
    if request.method == 'DELETE':
        return deleteEmployee(request, pk)