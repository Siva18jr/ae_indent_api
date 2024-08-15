from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes, name='routes'),
    path('outlets/', views.getOutlets, name='outlets'),
    path('outlet/<int:pk>/', views.getOutlet, name='outlet'),
    path('products/', views.getProducts, name='products'),
]