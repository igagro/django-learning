from django.contrib.auth import get_user_model

from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import Profile
from pkg.models import Role, Permission, RolePermission
from university.models import University, UniversitySchools
from school.models import School

User = get_user_model()


class MockAPITestCase(APITestCase):
    def setUp(self):
        """Setup 3 users: UniversityAdmin, SchoolAdmin and regular user"""
        self.university_admin = User.objects.create(username='universityAdmin')
        self.university_admin.set_password('M!stral123')
        self.university_admin.save()
        self.school_admin = User.objects.create(username='schoolAdmin')
        self.school_admin.set_password('M!stral123')
        self.school_admin.save()
        self.regular_user = User.objects.create_user(username='user')
        self.regular_user.set_password('M!stral123')
        self.regular_user.save()

        """Create roles"""
        self.unv_role = Role.objects.create(
            name='UniversityAdmin',
            role_type='UNV'
        )
        self.sch_role = Role.objects.create(
            name='SchoolAdmin',
            role_type='SCH'
        )

        """Create permissions"""
        self.add = Permission.objects.create(name='ADD')
        self.edit = Permission.objects.create(name='EDIT')
        self.delete = Permission.objects.create(name='DELETE')

        """Link roles with permissions"""
        RolePermission.objects.create(
            role=self.unv_role,
            permission=self.add
        )
        RolePermission.objects.create(
            role=self.unv_role,
            permission=self.edit
        )
        RolePermission.objects.create(
            role=self.unv_role,
            permission=self.delete
        )
        RolePermission.objects.create(
            role=self.sch_role,
            permission=self.add
        )
        RolePermission.objects.create(
            role=self.sch_role,
            permission=self.edit
        )
        RolePermission.objects.create(
            role=self.sch_role,
            permission=self.delete
        )

        """
        Create Profile objects (one2one with User) and add roles to profile
        """
        self.unv_admin_profile = Profile.objects.create(
            user=self.university_admin
        )
        self.unv_admin_profile.roles.add(self.unv_role.pk)
        self.sch_admin_profile = Profile.objects.create(
            user=self.school_admin
        )
        self.sch_admin_profile.roles.add(self.sch_role.pk)
        Profile.objects.create(
            user=self.regular_user)

        """Setup University"""
        self.university1 = University.objects.create(
            name="University1",
            address="Adress 1",
            city="City1",
            country=None,
            state=None,
            description="This is university description",
            logo_url=None
        )

        """Setup School"""
        self.school1 = School.objects.create(
            name="School1",
            address="Address 1",
            city="City1",
            country=None,
            state=None,
            description="This is school description",
            logo_url=None
        )

        """Setup UniversitySchool"""
        self.university_school1 = UniversitySchools.objects.create(
            university=University.objects.get(name="University1"),
            school=School.objects.get(name="School1"),
            is_main_school=True
        )
