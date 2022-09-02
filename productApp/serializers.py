from rest_framework import serializers
from productApp import models


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('uuid','title','price', 'seller')


class cardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.cardItem
        fields =['product', 'quantity', 'card']


class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.checkOut
        fields = ['items', 'address']

class cardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Card
        fields=('uuid','items',)

