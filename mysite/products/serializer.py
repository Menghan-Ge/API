from .models import Product
from .test import Message
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ['product_id', 'name']  # this name must equal the model.
        fields = "__all__"


class MessageSerializer(serializers.Serializer):
    class Meta:
        model = Message
        fields = ['email', 'content']
