from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings
from .models import *

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    # image_url = ProfileSerializer()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}


class ProfileSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'image_url',)

    def get_message(self, obj):
        return "Thank you for registering."

    def get_token_response(self, user):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        response = jwt_response_payload_handler(
            token, user, request=None)
        return response

    def create(self, validated_data):
        user_obj = validated_data.pop('user')
        user = UserRegisterSerializer.create(
            UserRegisterSerializer(), validated_data=user_data)
        profile, created = Profile.objects.update_or_create(
            user=user, image_url=validated_data.pop('iamge_url'))
        return profile
