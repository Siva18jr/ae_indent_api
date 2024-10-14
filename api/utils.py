from .models import Outlets, Product, OutletProducts, SaleProducts, Users, RemainingProducts
from .serializers import OutletSerializer, ProductSerializer, OutletProductsSerializer, SaleProductsSerializer, UserSerializer, CategorySerializer, RemainingProductsSerializer, OutletProductsCategorySerializer
from rest_framework.response import Response
from rest_framework import status
from .emails import sendOtpViaEmail
from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def getOutletList(request):
    
    outlets = Outlets.objects.all()
    serializer = OutletSerializer(outlets, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })

def getOutletDetail(request, pk):
    
    outlet = Outlets.objects.get(id=pk)
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

    data = request.data
    outlet = Outlets.objects.get(id=pk)
    serializer = OutletSerializer(instance=outlet, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'Outlet data updated'
        })
    else:
        print(serializer.errors)
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'Outlet data not updated'
        })
    

def deleteOutlet(request, pk):

    outlet = Outlets.objects.get(id=pk)
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

    data = request.data
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'Product data updated'
        })
    else:
        print(serializer.errors)
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'Product data not updated'
        })
    

def deleteProduct(request, pk):

    product = Product.objects.get(id=pk)
    product.delete()

    return Response({
        'status' : True,
        'message' : 'Product was deleted!'
    })

    
def getOutletProductsList(request):

    outlets = OutletProducts.objects.all()
    serializer = OutletProductsSerializer(outlets, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })


def addOutletProduct(request):
    
    serializer = OutletProductsSerializer(data=request.data)
    remaining = RemainingProductsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        if remaining.is_valid():
            remaining.save()
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
    

def getOutletProductsListByCategory(request):

    category = request.query_params.get('category')

    outlets = OutletProducts.objects.filter(product_category=category)
    serializer = OutletProductsSerializer(outlets, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })
    

def updateOutletProduct(request, pk):

    data = request.data
    product = OutletProducts.objects.get(id=pk)
    serializer = OutletProductsSerializer(instance=product, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'Product data updated'
        })
    else:
        print(serializer.errors)
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'Product data not updated'
        })
    

def deleteOutletProduct(request, pk):

    product = OutletProducts.objects.get(id=pk)
    product.delete()

    return Response({
        'status' : True,
        'message' : 'Product was deleted!'
    })
    

def getSaleProductsList(request):

    products = SaleProducts.objects.all()
    serializer = SaleProductsSerializer(products, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })


def addSaleProduct(request):

    data = {
        "product_details" : request.data['product_details'],
        "date":  request.data['date'],
        "outlet_name":  request.data['outlet_name'],
        "outlet_location":  request.data['outlet_location'],
        "outlet_number":  request.data['outlet_number'],
        "outlet_store_id":  request.data['outlet_store_id'],
        "cash": request.data['cash'],
        "balance" : request.data['balance'],
        "total" : request.data['total'],
        "shift" : request.data['shift']
    }
    
    serializer = SaleProductsSerializer(data=data)

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

    # loadData = {
    #     "id" : request.data['load_id'],
    #     "product_id" : request.data['product_id'],
    #     "shift":  request.data['shift'],
    #     "image_url": request.data['image_url'],
    #     "product_name":  request.data['name'],
    #     "product_price":  request.data['price'],
    #     "product_details":  request.data['details'],
    #     "product_category":  request.data['category'],
    #     "date":  request.data['load_date'],
    #     "quantity":  request.data['load_quantity']
    # }

    # product = OutletProducts.objects.get(id=request.data['load_id'])
    # loadSerializer = OutletProductsSerializer(instance=product, data=loadData)

    # if loadSerializer.is_valid():
    #     loadSerializer.save()

    #     remainingProducts = RemainingProducts.objects.get(id=request.data['load_id'])
    #     remainingProductsSerializer = OutletProductsSerializer(instance=remainingProducts, data=loadData)

    #     if remainingProductsSerializer.is_valid():
    #         remainingProductsSerializer.save()

    #     data = {
    #         "product_details" : request.data['product_details'],
    #         "date":  request.data['date'],
    #         "outlet_name":  request.data['outlet_name'],
    #         "outlet_location":  request.data['outlet_location'],
    #         "outlet_number":  request.data['outlet_number'],
    #         "outlet_store_id":  request.data['outlet_store_id'],
    #         "quantity":  request.data['quantity'],
    #         "cash": request.data['cash'],
    #         "balance" : request.data['balance']
    #     }
    
    #     serializer = SaleProductsSerializer(data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({
    #             'status' : True,
    #             'data' : serializer.data,
    #             'message' : 'New Product Updated'
    #         })
    #     else:
    #         return Response({
    #             'status' : False,
    #             'data' : serializer.data,
    #             'message' : 'Product not Updated'
    #         })
        
    # else:
    #     return Response({
    #         'status' : True,
    #         'data' : serializer.data,
    #         'message' : 'Product data updated'
    #     })
    

def updateSaleProduct(request, pk):

    data = request.data
    sale = SaleProducts.objects.get(id=pk)
    serializer = SaleProductsSerializer(instance=sale, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'Product data updated'
        })
    else:
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'Product data not updated'
        })
    
    
def getRemainingProductsList(request):

    date = request.query_params.get('date')
    shift = request.query_params.get('shift')

    products = RemainingProducts.objects.filter(date=date, shift=shift)
    serializer = RemainingProductsSerializer(instance=products, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })


def addRemainingProduct(request):
    
    serializer = RemainingProductsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'Remaining Product Updated'
        })
    else:
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'Remaining Product Updated'
        })
    

def updateRemainingProduct(request, pk):

    # request.data.get('name')

    data = request.data
    sale = RemainingProducts.objects.get(id=pk)
    serializer = RemainingProductsSerializer(instance=sale, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'Product data updated'
        })
    else:
        print(serializer.errors)
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'Product data not updated'
        })
    

def addUser(request):

    email = request.data['email']

    if Users.objects.filter(email=email).exists() is True:
        return Response({
                'status' : False,
                'data' : { },
                'message' : 'Email already exists'
        })
    else:
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
            'message' : 'Email exists'
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
    

def getCategories(request):

    products = Product.objects.all()
    serializer = CategorySerializer(products, many=True)

    categories = [data.get("category") for data in serializer.data]

    return Response({
        'data' : categories,
        'status' : status.HTTP_201_CREATED,
    })


def getSalesFilter(request):

    date = request.query_params.get('date')
    shift = request.query_params.get('shift')

    sales = SaleProducts.objects.filter(date=date, shift= shift)
    serializer = SaleProductsSerializer(instance=sales, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })


def getOutletProductsCategories(request):

    products = OutletProducts.objects.all()
    serializer = OutletProductsCategorySerializer(products, many=True)

    categories = [data.get("product_category") for data in serializer.data]

    return Response({
        'data' : categories,
        'status' : status.HTTP_201_CREATED,
    })


def getSalesDetails(request):

    outlet = request.query_params.get('outlet')

    sales = SaleProducts.objects.filter(outlet_name= outlet)
    serializer = SaleProductsSerializer(instance=sales, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })