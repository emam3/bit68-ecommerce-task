from rest_framework import permissions

class updateUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if(request.user.id == obj.id):
            return True

        # return False