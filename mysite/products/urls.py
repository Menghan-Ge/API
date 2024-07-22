from django.urls import path, include
from . import views
from products.views import ListProducts, ProductDetail

urlpatterns = [
    path('productlist/', views.listproducts, name='ListProduct'),
    path('messagelist/', views.listmessages, name='message'),
    path('classproductlist/', views.ListProducts.as_view(), name='listproducts'),
    path('classproductdetail/<int:pid>/', views.ProductDetail.as_view(), name='productdetail'),
]
