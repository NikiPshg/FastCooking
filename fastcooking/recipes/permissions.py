from rest_framework import permissions
import django_filters
from .models import Recipes


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


### service,filter
class CharFilterInFilter(filters.BaseInFilter):
    pass

class CategoryFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name = 'category', lookup_expr='in')
    class Meta:
        model = Recipes
        fields = ['category']

class RecipeModelFilter(django_filters.FilterSet):
    namedish = django_filters.CharFilter(field_name='namedish', lookup_expr='icontains')

    class Meta:
        model = Recipes
        fields = ['namedish']
