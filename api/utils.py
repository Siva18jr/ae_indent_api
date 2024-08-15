from .models import Outlet, Product
from .serializers import OutletSerializer, ProductSerializer
from rest_framework.response import Response

def getOutletList(request):
    
    outlets = Outlet.objects.all()
    serializer = OutletSerializer(outlets, many=True)

    return Response({
        'data' : serializer.data
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