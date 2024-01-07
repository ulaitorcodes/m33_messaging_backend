from django.contrib.auth import get_user_model
from rest_framework import serializers

from m33_messaging.users.models import User as UserType


User = get_user_model()


class UserSerializer(serializers.ModelSerializer[UserType]):
    class Meta:
        model = User
        fields = ["name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
        }

    
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user