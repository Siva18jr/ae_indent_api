from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes, name='routes'),
    path('outlets/', views.getOutlets, name='outlets'),
    path('outlet/<int:pk>/', views.getOutlet, name='outlet'),
    path('products/', views.getProducts, name='products'),
    path('product/<int:pk>/', views.getproduct, name='product'),
    path('outletproducts/', views.getOutletProducts, name='outlet products'),
    path('outletproduct/<int:pk>/', views.getOutletproduct, name='outlet product'),
    path('saleproducts/', views.getSaleProducts, name='sale products'),
    path('auth/', views.auth, name='auth'),
    path('verify/', views.verification, name='verification'),
    path('otp/', views.otp, name='otp')
]