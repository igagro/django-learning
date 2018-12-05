from django.conf import settings
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model


User = get_user_model()


def upload_profile_image(instance, filename):
    return "accounts/{user}/{filename}".format(user=instance.user,
                                               filename=filename)
