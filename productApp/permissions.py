from rest_framework import permissions
from usersApp.models import User

class AddNewProduct(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return (request.user.is_staff or request.user.is_seller)
        except Exception as e:
            return False

class createcartItemPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if(request.user.cart):
                return (True)
        except Exception as e:
            return False

    def has_object_permission(self, request, view, obj):
        try:
            cartOwner = User.objects.get(cart=obj.cart)
            return (cartOwner == request.user)
        except Exception as e:
            return False


class getcartPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if(request.user.cart):
                return (True)
        except Exception as e:
            return False
            
    def has_object_permission(self, request, view, obj):
        try:
            cartOwner = User.objects.get(cart=obj.cart)
            return (cartOwner == request.user)
        except Exception as e:
            return False