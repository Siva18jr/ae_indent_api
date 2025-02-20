from .models import Outlets, Product, OutletProducts, SaleProducts, Users, RemainingProducts, OutletPending
from .serializers import OutletSerializer, ProductSerializer, OutletProductsSerializer, SaleProductsSerializer, UserSerializer, CategorySerializer, RemainingProductsSerializer, OutletProductsCategorySerializer, OutletPendingSerializer
from rest_framework.response import Response
from rest_framework import status
from .emails import sendOtpViaEmail
from random import randint
import json

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

    storeId = request.data['storeId']

    if Outlets.objects.filter(storeId=storeId).exists() is True:
        return Response({
            'status' : False,
            'data' : {},
            'message' : 'Store Id already exists'
        })
    else:
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

    name = request.data['name']

    if Product.objects.filter(name=name).exists() is True:
        return Response({
            'status' : False,
            'data' : {},
            'message' : 'Product already exists'
        })
    else:
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

    name = request.data['product_name']
    shift = request.data['shift']
    date = request.data['date']

    if OutletProducts.objects.filter(product_name=name, date=date, shift=shift).exists() is True:
      
        outletProducts = OutletProducts.objects.get(product_name=name, date=date, shift=shift)
        remaining = RemainingProducts.objects.get(product_name=name, date=date, shift=shift)
        serializer = OutletProductsSerializer(outletProducts, many=False)
      
        data = {
            'product_id': request.data['product_id'], 
            'shift': shift,
            'image_url': request.data['image_url'], 
            'product_name': request.data['product_name'], 
            'product_price': request.data['product_price'], 
            'product_details': request.data['product_details'], 
            'product_category': request.data['product_category'],
            'emp_id': request.data['emp_id'], 
            'quantity': (int(serializer.data['quantity']) + int(request.data['quantity'])), 
            'date': date,
            'max_quantity' : (int(serializer.data['quantity']) + int(request.data['quantity']))
        }

        updateSerializer = OutletProductsSerializer(instance=outletProducts, data=data)
        updateremaining = RemainingProductsSerializer(instance=remaining, data=data)

        if updateSerializer.is_valid():
            updateSerializer.save()
            if updateremaining.is_valid():
                updateremaining.save()
            return Response({
                'status' : True,
                'data' : updateSerializer.data,
                'message' : 'Product data updated'
            })
        else:
            return Response({
                'status' : False,
                'data' : updateSerializer.data,
                'message' : 'Product data not updated'
            })

    else:
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
        "shift" : request.data['shift'],
        "emp_id" : request.data['emp_id']
    }
    
    serializer = SaleProductsSerializer(data=data)

    if serializer.is_valid():
        
        serializer.save()
        
        productDetails = request.data['product_details']

        productData = json.loads(productDetails)

        for item in productData:

            remainingQuantity = (int(item['max_quantity']) - int(item['quantity']))

            remainingProductData = {
                "id" : item['id'],
                "product_id" : item['product_id'],
                "shift": item['shift'],
                "image_url": item['image_url'],
                "product_name": item['product_name'],
                "product_price": item['product_price'],
                "product_details": item['product_details'],
                "product_category": item['product_category'],
                "date": item['date'],
                "total_product_price" : remainingQuantity * int(item['product_price']),
                "quantity": remainingQuantity,
                "max_quantity" : item['quantity'],
                "emp_id" : item['emp_id']
            }
        
            remaining = RemainingProducts.objects.get(id=item["id"])
            remainingProductsSerializer = RemainingProductsSerializer(instance=remaining, data=remainingProductData)

            load = OutletProducts.objects.get(id=item["id"])
            outletProductsSerializer = OutletProductsSerializer(instance=load, data=remainingProductData)

            if outletProductsSerializer.is_valid():
                outletProductsSerializer.save()

            if remainingProductsSerializer.is_valid():
                remainingProductsSerializer.save()

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
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'Product data not updated'
        })
    

def addUser(request):

    email = request.data['email']
    empId = request.data['emp_id']

    if Users.objects.filter(email=email).exists() is True:
        return Response({
                'status' : False,
                'data' : { },
                'message' : 'Email already exists'
        })
    else:
        if Users.objects.filter(emp_id=empId).exists() is True:
            return Response({
                'status' : False,
                'data' : { },
                'message' : 'Employee Id already exists'
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
                'status' : False,
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

    sales = SaleProducts.objects.filter(date=date, shift=shift)
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

    sales = SaleProducts.objects.filter(outlet_name=outlet)
    serializer = SaleProductsSerializer(instance=sales, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })


def getSalesProductDetails(request):

    outlet = request.query_params.get('outlet')
    shift = request.query_params.get('shift')
    date = request.query_params.get('date')

    sales = SaleProducts.objects.filter(outlet_name=outlet, shift=shift, date=date)
    serializer = SaleProductsSerializer(instance=sales, many=True)

    productData = []

    for entry in serializer.data:
        product_details = json.loads(entry["product_details"])
        productData.extend(product_details)

    return Response({
        'data' : productData,
        'status' : status.HTTP_201_CREATED
    })


def updateOutletPending(request):

    outlet = request.data['outlet']

    if OutletPending.objects.filter(outlet=outlet).exists() is True:

        pending = OutletPending.objects.get(outlet=outlet)
        serializer = OutletPendingSerializer(instance=pending, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : True,
                'data' : serializer.data,
                'message' : 'Outlet Pending Updated'
            })
        else:
            return Response({
                'status' : False,
                'data' : { },
                'message' : serializer.errors
            })
        
    else:
        serializer = OutletPendingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : True,
                'data' : serializer.data,
                'message' : 'Outlet Pending Updated'
            })
        else:
            return Response({
                'status' : False,
                'data' : { },
                'message' : serializer.errors
            })
        

def getOutletPending(request):

    outlet = request.query_params.get('outlet')

    if OutletPending.objects.filter(outlet=outlet).exists() == True:
        
        outlet = OutletPending.objects.get(outlet=outlet)
        serializer = OutletPendingSerializer(instance=outlet, many=False)

        return Response({
            'data' : serializer.data,
            'status' : status.HTTP_201_CREATED
        })
    else:
        return Response({
            'data' : { },
            'status' : status.HTTP_201_CREATED
        })
    

def getEmployees(request):

    users = Users.objects.filter(type='employee')
    serializer = UserSerializer(instance=users, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })


def getRecentEmployees(request):

    users = Users.objects.filter(type='employee').order_by('created')[:5]
    serializer = UserSerializer(instance=users, many=True)

    return Response({
        'data' : serializer.data,
        'status' : status.HTTP_201_CREATED
    })


def updateEmployeeData(request, pk):

    data = request.data
    users = Users.objects.get(id=pk)
    serializer = UserSerializer(instance=users, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'Employee data updated'
        })
    else:
        return Response({
            'status' : False,
            'data' : serializer.data,
            'message' : 'Employee data not updated'
        })
    

def deleteEmployee(request, pk):

    user = Users.objects.get(id=pk)
    user.delete()

    return Response({
        'status' : True,
        'message' : 'Employee deleted!'
    })