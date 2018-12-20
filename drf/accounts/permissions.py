from rest_framework import permissions


class AnnonPermisionOnly(permissions.BasePermission):
    """
    Non-authenticated users only
    """

    def has_permission(self, request, view):
        return not request.user.is_authenticated
