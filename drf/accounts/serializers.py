from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db import transaction
from .utils import *
from .models import *

User = get_user_model()

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterSerializer(serializers.ModelSerializer):
    token_response = serializers.SerializerMethodField(read_only=True)

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'token_response'
        ]

    def get_token_response(self, user):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        response = jwt_response_payload_handler(token)
        return response


class ProfileSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer()
    message = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'image_url', 'message', 'roles')

    extra_kwargs = {'image_url': {'required': False}}

    def get_message(self, obj):
        return "Thank you for registering."

    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data['password']
        user_data['password'] = make_password(password)
        user = UserRegisterSerializer.create(
            UserRegisterSerializer(), validated_data=user_data)
        profile = Profile.objects.create(
            user=user,
            image_url=validated_data.pop('image_url'),
        )
        profile.roles.add(*validated_data['roles'])
        return profile
