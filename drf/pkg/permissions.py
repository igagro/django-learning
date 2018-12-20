from rest_framework import permissions
from accounts.models import Profile
from pkg.models import Role, Permission, RolePermission
from django.db.models import Q
from university.models import University, School, UniversitySchools

ADD = 1
EDIT = 2
DELETE = 3


class CanAddUniversity(permissions.BasePermission):
    """
    Permission for create or read university
    """
    message = "Adding university objects not allowed"

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        """
        Only user with roles who have UNV role_type and ADD permission
        can create University
        """

        return RolePermission.objects.filter(
            role__role_type='UNV',
            permission=ADD,
            role__profiles=request.user.profile
        ).exists()


class CanAddSchool(permissions.BasePermission):
    """
    Permission for create or read school
    """
    message = "Adding school objects not allowed"

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        """
        Only user with roles who have SCH role_type and ADD permission
        can create School
        """

        return RolePermission.objects.filter(
            role__role_type='SCH',
            permission=ADD,
            role__profiles=request.user.profile
        ).exists()


class CanEditOrRemoveUniversity(permissions.BasePermission):
    """
    Permission allow user to edit or delete University object
    """
    message = "Editing or removing university objects not allowed"

    def has_object_permission(self, request, view, obj):
        """
        Only user with roles who have UNV role_type
        and EDIT and DELETE permissions
        can edit or remove University
        """

        return RolePermission.objects.filter(
            role__role_type='UNV',
            permission__in=[ADD, DELETE],
            role__profiles=request.user.profile
        ).exists()


class CanEditOrRemoveSchool(permissions.BasePermission):
    """
    Permission allow user to edit or delete School object
    """
    message = "Editing or removing school objects not allowed"

    def has_object_permission(self, request, view, obj):
        """
        Only user with roles who have SCH role_type
        and EDIT and DELETE permissions
        can edit or remove School
        """

        return RolePermission.objects.filter(
            role__role_type='SCH',
            permission__in=[ADD, DELETE],
            role__profiles=request.user.profile
        ).exists()
