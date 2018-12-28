from rest_framework.reverse import reverse
from rest_framework import status

from pkg.mockup_test_setup import MockAPITestCase
from school.models import School


class SchoolAPITestCase(MockAPITestCase):
    """School API Test case"""

    def test_get_schools(self):
        """Test if any user can get list of schools"""
        url = reverse('school:school-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_school(self):
        """Test create school with given permissions"""
        self.client.login(
            username='schoolAdmin',
            password='M!stral123'
        )
        url = reverse('school:school-list')
        data = {
            "name": "School2",
            "address": "Address2",
            "city": "City2",
            "country": None,
            "state": None,
            "description": "",
            "logo_url": None
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_school(self):
        """Test update school with given permissions"""
        self.client.login(
            username='schoolAdmin',
            password='M!stral123'
        )
        url = reverse(
            'school:school-detail',
            args=[self.school1.pk]
        )
        data = {
            "name": "School2",
            "address": "Address2",
            "city": "City2",
            "country": None,
            "state": None,
            "description": "",
            "logo_url": None
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])

    def test_delete_school(self):
        """Test delete school with given permissions"""
        self.client.login(
            username='schoolAdmin',
            password='M!stral123'
        )
        url = reverse(
            'school:school-detail',
            args=[self.school1.pk]
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(School.DoesNotExist):
            School.objects.get(pk=self.school1.pk)
