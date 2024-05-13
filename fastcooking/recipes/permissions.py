from rest_framework import permissions
from django_filters import rest_framework as filters
from .models import Recipes


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


### service
class CharFilterInFilter(filters.BaseInFilter):
    pass

class CategoryFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name = 'category', lookup_expr='in')
    class Meta:
        model = Recipes
        fields = ['category']

