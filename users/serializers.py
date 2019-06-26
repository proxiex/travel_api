"""Users serializer."""

import os
from django.conf import settings
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    """Users serialzers class."""

    class Meta:
        """Meta class."""

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
    """Token data serializer."""

    token = serializers.CharField(max_length=255)


class ProfileSerializer(serializers.ModelSerializer):
    """Profile serializer."""

    class Meta:
        """Meta class."""

        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'gender',
            'dob',
            'profile_img'
        ]

        read_only_fields = ('email', 'username')

        model = models.CustomUser

    def validate(self, data):
        """Validate uploaded file.

        - maximum image size: 2MB
        - only images
        """
        max_upload_size = settings.MAX_UPLOAD_SIZE
        _file = data['profile_img']
        if _file:
            ext = os.path.splitext(_file.name)[1]
            valid_extensions = ['.png', '.jpg', '.jpeg', '.webp']
            if not ext.lower() in valid_extensions:
                raise serializers.ValidationError(u'Unsupported file type.')
            if _file.size > max_upload_size:
                raise serializers.ValidationError(u'Image size must not exceed 2MB ')
            return data
