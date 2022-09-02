from rest_framework import serializers
from productApp import models


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('uuid','title','price', 'seller')


class cartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.cartItem
        fields =['product', 'quantity', 'cart']


class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.checkOut
        fields = ['items', 'address']

class cartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields=('uuid','items',)

