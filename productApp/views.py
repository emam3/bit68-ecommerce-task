from json import JSONDecoder
from msilib.schema import Error
from tokenize import Token
from urllib import request
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from productApp import serializers
from productApp.models import Cart, Product, cartItem, checkOut
from rest_framework.authentication import TokenAuthentication
from productApp.permissions import AddNewProduct, createcartItemPermission, getcartPermission

# Create your views here.


class createProductView(viewsets.ModelViewSet):
    serializer_class = serializers.productSerializer
    permission_classes = (AddNewProduct,)
    authentication_classes = (TokenAuthentication,)
    queryset = Product.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)
    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        is_staff = self.request.user.is_staff
        queryset = queryset.filter(seller=10) if not is_staff else queryset
        return queryset
    

    def create(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            if(serializer.validated_data['seller'] != request.user):
                return Response({
                    'Error' : "You're not allowed to perform this action"
                })
            product = Product.objects.create(
                title = serializer.validated_data['title'],
                price = serializer.validated_data['price'],
                seller = serializer.validated_data['seller']
            )
            product.save()
            return Response({
                'product_uuid' : product.uuid,
                'product title' : product.title,
                'poduct_price' : product.price
            })

        except Exception as e:
            return Response({
                'Error' : 'something went wrong while creating new product',
                'Reason' : str(e)
            })

class getAllProducts(viewsets.ModelViewSet):
    serializer_class = serializers.productSerializer
    queryset = Product.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)

class getcart(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (getcartPermission,)
    serializer_class = serializers.cartSerializer
    queryset = Cart.objects.all()
    def get_queryset(self):
        self.queryset = self.request.user.cart
        return [self.queryset]

class createcartItemView(viewsets.ModelViewSet):
    serializer_class = serializers.cartItemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (createcartItemPermission,)
    queryset = cartItem.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        cart = self.request.user.cart
        is_staff = self.request.user.is_staff
        queryset = queryset.filter(cart=cart) if not is_staff else queryset

        return queryset

    def create(self,request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            if serializer.validated_data['cart'] != request.user.cart:
                return Response({
                    "apiStatus" : False,
                    "Reason": "you're not allowed to"
                })
            item = cartItem.objects.create(
                product = serializer.validated_data['product'],
                quantity = serializer.validated_data['quantity'],
                cart = serializer.validated_data['cart']
            )
            item.save()
            cart = request.user.cart
            cart.items.add(item)
            return Response({
                'item_uuid' : item.uuid,
                'item_product': item.product.title,
                'item_quantity':item.quantity
            })

        except Exception as e:
            return Response({
                'Error' : 'something went wrong while creating new product',
                'Reason' : str(e)
            })


class createOrderView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.orderSerializer
    queryset = checkOut.objects.all()
    total_price = 0
    def create(self,request):
        """Before creating the checkout we have to check whether the items are in the request.user.cart or not"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        items = serializer.validated_data['items']
        user_cart = request.user.cart
        for item in items:
            self.total_price += item.itemPrice 
            if item.cart != user_cart:
                return Response({
                    'Error' : "You're not allowed to perform this action"
                })
        checkout = checkOut.objects.create(
            address = serializer.validated_data['address'],
            totalPrice = self.total_price,
            user = request.user
        )
        checkout.items.set(items)

        user_cart.items.remove(*items)
        return Response({
            "checkout_uuid" : checkout.uuid,
            "checkout_price" : checkout.totalPrice,
            "checkout_user" : str(request.user.get_full_name())
            })


class getUserOrders(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.orderSerializer
    queryset = checkOut.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        is_staff = self.request.user.is_staff
        queryset = queryset.filter(user=user) if not is_staff else queryset
        return queryset

