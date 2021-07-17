from rest_framework import serializers 
from .models import UserAccount 

from django.contrib.auth import get_user_model
User = get_user_model()

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = "__all__"
        fields = ["id","email", 'name', 'is_active', 'is_superuser', "last_login", "is_staff" , ]

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
