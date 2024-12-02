from rest_framework.serializers import ModelSerializer
from .models import Outlets, Product, OutletProducts, SaleProducts, Users, RemainingProducts, OutletPending

class OutletSerializer(ModelSerializer):
    
    class Meta:
        model = Outlets
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'


class OutletProductsSerializer(ModelSerializer):
    
    class Meta:
        model = OutletProducts
        fields = '__all__'


class SaleProductsSerializer(ModelSerializer):
   
    class Meta:
        model = SaleProducts
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['category']


class RemainingProductsSerializer(ModelSerializer):

    class Meta:
        model = RemainingProducts
        fields = '__all__'


class OutletProductsCategorySerializer(ModelSerializer):

    class Meta:
        model = OutletProducts
        fields = ['product_category']


class OutletPendingSerializer(ModelSerializer):

    class Meta:
        model = OutletPending
        fields = '__all__'