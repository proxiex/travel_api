"""Flights permission module."""

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUserOrReadOnly(BasePermission):
    """Is adim class."""

    def has_permission(self, request, view):
        """Only super users can create, edit and delete flights.normal users are allowed to only view flights."""
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_staff
