from rest_framework import permissions
from accounts.models import Profile
from pkg.models import Role, Permission, RolePermission
from django.db.models import Q
from university.models import University, School, UniversitySchools

ADD = 1
EDIT = 2
DELETE = 3


class CanAddObject(permissions.BasePermission):
    """
    Permission for create or read university
    """
    message = "Adding university objects not allowed"

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        """
        TO DO
        Need to check how to pass queryset 
        from UniversitySchools to has_permission arg "view"
        This is temporary solution
        """
        role_type = None

        if view.queryset is not None:
            if view.queryset.model is University:
                role_type = 'UNV'
            elif view.queryset.model is School:
                role_type = 'SCH'
        else:
            role_type = 'UNV'

        """
        Only user with roles who have UNV role_type and ADD permission
        can create University
        """

        if RolePermission.objects.filter(
            role__role_type=role_type,
            permission=ADD,
            role__profiles=request.user.profile
        ).exists():
            return True
        else:
            return False


class CanEditOrRemoveObject(permissions.BasePermission):
    """
    Permission allow user to edit or delete university object
    """
    message = "Editing or removing university objects not allowed"

    def has_object_permission(self, request, view, obj):
        """
        Only user with roles who have UNV role_type
        and EDIT and DELETE permissions
        can edit or remove University
        """
        role_type = None

        if obj._meta.concrete_model is University:
            role_type = 'UNV'
        elif obj._meta.concrete_model is School:
            role_type = 'SCH'
        else:
            role_type = 'UNV'

        if RolePermission.objects.filter(
            role__role_type=role_type,
            permission__in=[ADD, DELETE],
            role__profiles=request.user.profile
        ).exists():
            return True
        else:
            return False
