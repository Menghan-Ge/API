from django.urls import path, include
from . import views
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

# router = DefaultRouter()
router = SimpleRouter()
router.register('productviewset', ProductViewSet, basename='product')


urlpatterns = [
    path('productlist/', views.listproducts, name='ListProduct'),
    path('messagelist/', views.listmessages, name='message'),
    path('classproductlist/', views.ListProducts.as_view(), name='listproducts'),
    path('classproductdetail/<int:pid>/', views.ProductDetail.as_view(), name='productdetail'),
    path('mixinpath/', views.ListProductMixins.as_view(), name='mp'),
    path('productmixin/<int:pk>', views.DetailedProductMixins.as_view(), name='mdp'),
    path('productgenericlist/', views.ListProductsGenerics.as_view(), name='lpg'),
    path('productgenericdetail/<int:pk>/', views.DetailedProductGenerics.as_view(), name='dpg'),
    path('special/<int:pk>', views.SpecialProductGenerics.as_view(), name='spg'),
] + router.urls
