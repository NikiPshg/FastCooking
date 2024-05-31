from django_filters import rest_framework as filters
from .models import Recipes
from django.db.models import Q

### service
class CharFilterInFilter(filters.BaseInFilter):
    pass

class CategoryFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name = 'category', lookup_expr='in')
    class Meta:
        model = Recipes
        fields = ['category']

class RecipesFilter(filters.FilterSet):
    namedish = filters.CharFilter(field_name='namedish', method='filter_namedish')

    def filter_namedish(self, queryset, name, value):
        return queryset.filter(Q(namedish__icontains=value))

    class Meta:
        model = Recipes
        fields = ['namedish']