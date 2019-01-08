from rest_framework.reverse import reverse
from rest_framework import status

from pkg.mockup_test_setup import MockAPITestCase
from university.models import University, UniversitySchools


class UniversityAPITestCase(MockAPITestCase):
    """University and UniversitySchool API Test case"""

    def test_get_universities(self):
        """Test if any user can get list of universities"""
        url = reverse('university:university-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_university(self):
        """Test create university with given permissions"""
        self.client.login(
            username='universityAdmin',
            password='M!stral123'
        )
        url = reverse('university:university-list')
        data = {
            "name": "University2",
            "address": "Address2",
            "city": "City2",
            "country": None,
            "state": None,
            "description": "",
            "logo_url": None
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        """
        User without add permission shouldn't be able to create university
        """
        self.client.login(
            username='schoolAdmin',
            password='M!stral123'
        )
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_university(self):
        """Test update university with given permissions"""
        self.client.login(
            username='universityAdmin',
            password='M!stral123'
        )
        url = reverse(
            'university:university-detail',
            args=[self.university1.pk]
        )
        data = {
            "name": "University2",
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
        """
        User without edit permission
        shouldn't be able to edit university
        """
        self.client.login(
            username='user',
            password='M!stral123'
        )
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_university(self):
        """Test delete university with given permissions"""
        self.client.login(
            username='universityAdmin',
            password='M!stral123'
        )
        url = reverse(
            'university:university-detail',
            args=[self.university1.pk]
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(University.DoesNotExist):
            University.objects.get(pk=self.university1.pk)

    def test_get_university_schools(self):
        """Test if any user can get list of university schools"""
        url = reverse(
            'university:university_schools_list',
            args=[self.university1.pk]
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_university_schools(self):
        """Test create school for university with given permissions"""
        self.client.login(
            username='universityAdmin',
            password='M!stral123'
        )
        url = reverse(
            'university:university_schools_list',
            args=[self.university1.pk]
        )
        data = {
            "school": {
                "name": "School3",
                "address": "Address3",
                "city": "City3",
                "country": None,
                "state": None,
                "description": "",
                "logo_url": None
            },
            "is_main_school": True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        """
        User without add permission
        shouldn't be able to create school for university
        """
        self.client.login(
            username='user',
            password='M!stral123'
        )
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_university_school(self):
        """Test update university school with given permissions"""
        self.client.login(
            username='universityAdmin',
            password='M!stral123'
        )
        url = reverse(
            'university:university_school_detail',
            args=[self.university1.pk, self.school1.pk]
        )
        data = {
            "school": {
                "name": "SchoolEdit",
                "address": "Address3",
                "city": "City3",
                "country": None,
                "state": None,
                "description": "",
                "logo_url": None
            },
            "is_main_school": False
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['is_main_school'],
            data['is_main_school']
        )
        """
        User without edit permission
        shouldn't be able to edit school of university
        """
        self.client.login(
            username='user',
            password='M!stral123'
        )
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_university_school(self):
        """Test delete school of university with given permissions"""
        self.client.login(
            username='universityAdmin',
            password='M!stral123'
        )
        url = reverse(
            'university:university_school_detail',
            args=[self.university1.pk, self.school1.pk]
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(UniversitySchools.DoesNotExist):
            UniversitySchools.objects.get(pk=self.university_school1.pk)
