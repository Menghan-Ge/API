from django.shortcuts import render
from .models import Product
from .serializer import ProductSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .test import Message
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
# @permission_classes(IsAuthenticated)
def listproducts(request):
    products = Product.objects.all()  # there is so many produts will be there it can be tricked.
    serializer_class = ProductSerializer(products, many=True)
    # many = true is applicable when you have the iterated data
    return Response(serializer_class.data)


@api_view(['GET', 'POST'])
def listmessages(request):
    message_obj = Message('admin@admin.io', 'Hello...')
    serializer_class = MessageSerializer(message_obj)
    return Response(serializer_class.data)


class ListProducts(APIView):
    def get(self, request):
        query = Product.objects.all()
        serializer_class = ProductSerializer(query, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        serializer_obj = ProductSerializer(data=request.data)
        if serializer_obj.is_valid(raise_exception=True):
            product_saved = serializer_obj.save()
            return Response(f"Success: Product {product_saved.name} created successfully")

        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):

    def get(self, request, pid):
        query = Product.objects.filter(product_id=pid)
        serializer_class = ProductSerializer(query, many=True)
        return Response(serializer_class.data)

    def put(self, request, pid):
        product_obj = Product.objects.get(product_id=pid)
        serializer_obj = ProductSerializer(product_obj, data=request.data)
        if serializer_obj.is_valid(raise_exception=True):
            product_saved = serializer_obj.save()
            return Response("Success: Product'{}' updated successfully".format(product_saved.name))
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pid):
        Product.objects.get(product_id=pid).delete()
        return Response(status=status.HTTP_200_OK)
