from .models import Product
from .test import Message
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ['product_id', 'name']  # this name must equal the model.
        fields = "__all__"


class MessageSerializer(serializers.Serializer):
    model = Message
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateField()
