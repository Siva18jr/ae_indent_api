from rest_framework.serializers import ModelSerializer
from .models import Outlet, Product, OutletProducts, SaleProducts, Users

class OutletSerializer(ModelSerializer):
    class Meta:
        model = Outlet
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