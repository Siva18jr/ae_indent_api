from django.contrib import admin
from . models import Outlets, Product, OutletProducts, RemainingProducts, SaleProducts, Users

admin.site.register(Outlets)
admin.site.register(Product)
admin.site.register(OutletProducts)
admin.site.register(RemainingProducts)
admin.site.register(SaleProducts)
admin.site.register(Users)