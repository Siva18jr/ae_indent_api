from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes, name='routes'),
    path('outlets/', views.getOutlets, name='outlets'),
    path('outlet/<int:pk>/', views.getOutlet, name='outlet'),
    path('products/', views.getProducts, name='products'),
    path('product/<int:pk>/', views.getproduct, name='product'),
    path('load/products/', views.getOutletProducts, name='load products'),
    path('load/product/<int:pk>/', views.getOutletproduct, name='outlet product'),
    path('sales/products/', views.getSaleProducts, name='sale products'),
    path('saleproduct/<int:pk>/', views.getSaleproduct, name='sale product'),
    path('auth/', views.auth, name='auth'),
    path('verify-email/', views.verification, name='emailverification'),
    path('auth/otp', views.otp, name='otp'),
    path('categories/', views.getCategory, name='categories'),
    path('products/remaining', views.getRemainingProducts, name='remaining products'),
    path('remainingproduct/<int:pk>/', views.getRemainingproduct, name='remaining product'),
    path('sales/filter', views.getFilteredSales, name='filtered sales'),
    path('load/products/category', views.getOutletProductsByCategory, name='load products by category'),
    path('load/category', views.getOutletProductsCategory, name='load categories'),
    path('sales/outlets/detail', views.getSalesDetail, name='sales detail')
]