from django.contrib.auth import get_user_model

from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Profile
from pkg.models import Role

User = get_user_model()


class UserAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username="user1", email="user1@gmail.com")
        user.set_password("djangoapp")
        user.save()
        Profile.objects.create(user=user)
        Role.objects.create(name='UniversityAdmin', role_type='UNV')
        Role.objects.create(name='SchoolAdmin', role_type='SCH')

    def test_created_user(self):
        user = User.objects.filter(username="user1")
        profile = Profile.objects.filter(user=user[0])
        self.assertEqual(user.exists(), True)
        self.assertEqual(profile.exists(), True)

    def test_register_user_api(self):
        UNV_admin_role = Role.objects.get(name='UniversityAdmin')
        SCH_admin_role = Role.objects.get(name='SchoolAdmin')
        url = reverse('accounts:register')
        data = {
            'user': {
                'email': '',
                'first_name': '',
                'last_name': '',
                'password': 'djangoapp',
                'username': 'user2'
            },
            'roles': [UNV_admin_role.pk, SCH_admin_role.pk],
            'image_url': None
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user_api(self):
        url = reverse('accounts:login')
        data = {
            'username': 'user1',
            'password': 'djangoapp'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_user_api_fail(self):
        url = reverse('accounts:login')
        data = {
            'username': 'user2',
            'password': 'djangoapp'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
