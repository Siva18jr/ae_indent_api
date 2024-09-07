from django.contrib import admin
from . models import Outlet, Product, OutletProducts

admin.site.register(Outlet)
admin.site.register(Product)
admin.site.register(OutletProducts)