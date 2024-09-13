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
    path('saleproduct/<int:pk>/', views.getSaleproduct, name='sale product'),
    path('auth/', views.auth, name='auth'),
    path('verify/', views.verification, name='verification'),
    path('otp/', views.otp, name='otp'),
    path('categories/', views.getCategory, name='categories'),
    path('remainingproducts/', views.getRemainingProducts, name='remaining products'),
    path('remainingproduct/<int:pk>/', views.getRemainingproduct, name='remaining product'),
    path('salesfilter/', views.getFilteredSales, name='filtered sales'),
]