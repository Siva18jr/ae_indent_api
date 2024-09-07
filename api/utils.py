from .models import Outlet, Product, OutletProducts, SaleProducts, Users
from .serializers import OutletSerializer, ProductSerializer, OutletProductsSerializer, SaleProductsSerializer, UserSerializer
from rest_framework.response import Response
from django.http import QueryDict
from rest_framework import status
from .emails import sendOtpViaEmail
from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def getOutletList(request):
    
    # order_id = request.query_params.get('order_id')
    # request.query_params['testData']
    outlets = Outlet.objects.all()
    serializer = OutletSerializer(outlets, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })

def getOutletDetail(request, pk):
    
    outlet = Outlet.objects.get(id=pk)
    serializer = OutletSerializer(outlet, many=False)
    
    return Response(serializer.data)


def createOutlet(request):
    
    serializer = OutletSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'New outlet created'
        })
    else:
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'Outlet not created'
        })
    

def updateOutlet(request, pk):

    # request.data.get('name')

    data = request.data
    outlet = Outlet.objects.get(id=pk)
    serializer = OutletSerializer(instance=outlet, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'Outlet data not updated'
        })
    else:
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'outlet data updated'
        })
    

def deleteOutlet(request, pk):

    outlet = Outlet.objects.get(id=pk)
    outlet.delete()

    return Response({
        'status' : True,
        'message' : 'Outlet was deleted!'
    })


def getProductList(request):
    
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response({
        'data' : serializer.data
    })


def addProduct(request):
    
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'New Product Added'
        })
    else:
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'Product not added'
        })
    

def updateProduct(request, pk):

    # request.data.get('name')

    data = request.data
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'Product data not updated'
        })
    else:
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'Product data updated'
        })
    

def deleteProduct(request, pk):

    outlet = Product.objects.get(id=pk)
    outlet.delete()

    return Response({
        'status' : True,
        'message' : 'Product was deleted!'
    })

    
def getOutletProducts(request):

    outlets = OutletProducts.objects.all()
    serializer = OutletSerializer(outlets, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })


def addOutletProduct(request):
    
    serializer = OutletProductsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'New Product Added'
        })
    else:
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'Product not added'
        })
    

def updateOutletProduct(request, pk):

    # request.data.get('name')

    data = request.data
    product = OutletProducts.objects.get(id=pk)
    serializer = OutletProductsSerializer(instance=product, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'Product data not updated'
        })
    else:
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'Product data updated'
        })
    

def getSaleProducts(request):

    outlets = SaleProducts.objects.all()
    serializer = OutletSerializer(outlets, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })


def addSaleProduct(request):
    
    serializer = SaleProductsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'New Product Updated'
        })
    else:
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'Product not Updated'
        })
    

def addUser(request):
    
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'Account registered'
        })
    else:
        field_names = []
        for field_name, field_errors in serializer.errors.items():
            field_names.append(field_name)
        return Response({
            # 'status' : status.HTTP_400_BAD_REQUEST,
            'status' : False,
            'data' : { },
            'message' : f'Invalid data in {field_names}'
        })
    

def login(request):

    emailData = request.query_params.get('email')

    if Users.objects.filter(email=emailData).exists() is True:
        users = Users.objects.get(email=emailData)
        serializer = UserSerializer(instance = users, many= False)
        if(serializer.data['password'] == request.query_params.get('password')):
            return Response({
                'status' : True,
                'data' : serializer.data,
                'message' : 'User Verified'
            })
        else:
            return Response({
                'status' : True,
                'data' : { },
                'message' : 'Wrong crendential'
            })

    else:
        return Response({
            'status' : False,
            'data' : { },
            'message' : 'Email not exists'
        })
    

def verifyEmail(request):

    emailData = request.query_params.get('email')

    if Users.objects.filter(email=emailData).exists() is True:
         return Response({
            'status' : True,
            'data' : { },
            'message' : 'Email verified'
        })

    else:
        return Response({
            'status' : False,
            'data' : { },
            'message' : 'Email not exists'
        })
    

def sendOtp(request):

    emailData = request.query_params.get('email')

    try:
        otp = random_with_N_digits(6)
        sendOtpViaEmail(emailData, otp)
        return Response({
            'status' : True,
            'data' : otp,
            'message' : 'Verification Email Sent'
        })
    except:
        return Response({
            'status' : False,
            'data' : 0,
            'message' : 'Email not Sent'
        })