from django.shortcuts import render
from .models import Product
from .serializer import ProductSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .test import Message

# Create your views here.


@api_view(['GET', 'POST'])
@permission_classes(IsAuthenticated)
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
