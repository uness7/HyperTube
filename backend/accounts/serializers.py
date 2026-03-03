from rest_framework import serializers
from django.contrib.auth import get_user_model
from typing import Dict, Any

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")

    def create(self, validated_data: Dict[str, Any]):
        return User.objects.create_user(**validated_data)
