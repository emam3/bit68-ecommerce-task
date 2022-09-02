from rest_framework import permissions
from usersApp.models import User

class AddNewProduct(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return (request.user.is_staff or request.user.is_seller)
        except Exception as e:
            return False

class createCardItemPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if(request.user.card):
                return (True)
        except Exception as e:
            return False

    def has_object_permission(self, request, view, obj):
        try:
            cardOwner = User.objects.get(card=obj.card)
            return (cardOwner == request.user)
        except Exception as e:
            return False


class getCardPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if(request.user.card):
                return (True)
        except Exception as e:
            return False
            
    def has_object_permission(self, request, view, obj):
        try:
            cardOwner = User.objects.get(card=obj.card)
            return (cardOwner == request.user)
        except Exception as e:
            return False