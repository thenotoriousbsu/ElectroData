from rest_framework.permissions import BasePermission

class IsActiveUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_active


# class IsOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.user_id == request.user
