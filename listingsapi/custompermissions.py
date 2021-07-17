from rest_framework.permissions import BasePermission
from rest_framework import permissions 
class ExpensePermission(BasePermission):
    def has_permission(self,request,view):
        WRITE_METHODS=("POST", "PUT",)
        return (
            request.method in WRITE_METHODS or
            request.user and
            request.user.is_superuser
        )
