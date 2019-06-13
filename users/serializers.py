from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'password': {'write_only': True}
        }
        model = models.CustomUser
        fields = [
            'email',
            'username',
            'password',
        ]


class TokenSerializer(serializers.Serializer):
    """
    token data serializer
    """
    token = serializers.CharField(max_length=255)