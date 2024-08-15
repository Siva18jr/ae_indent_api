from rest_framework.serializers import ModelSerializer

from . models import Outlet, Product

class OutletSerializer(ModelSerializer):
    class Meta:
        model = Outlet
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'