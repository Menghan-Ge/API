from django.urls import path, include
from . import views

urlpatterns = [
    path('productlist/', views.listproducts, name='ListProduct'),
    path('messagelist/', views.listmessages, name='message'),
]
