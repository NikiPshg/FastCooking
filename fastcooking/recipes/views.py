from rest_framework import generics
from rest_framework import viewsets
#from django.shortcuts import render
from .models import Recipes
from .serializers import RecipeSerializer
from .permissions import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as django_filters,filters
from django_filters import rest_framework as filters
from django.db.models.functions import Lower
from rest_framework.response import Response
from rest_framework.views import APIView





#фильтр, поиск
class RecipesFilter(filters.FilterSet):
    namedish = filters.CharFilter(field_name='namedish', method='filter_namedish')

    def filter_namedish(self, queryset, name, value):
        return queryset.annotate(lower_namedish=Lower('namedish')).filter(lower_namedish__icontains=value.lower())

    class Meta:
        model = Recipes
        fields = ['namedish']
#фильтрация категории
class CategoryFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(method='filter_by_category')

    class Meta:
        model = Recipes
        fields = ['category']

    def filter_by_category(self, queryset, name, value):
        if value == '1':
            return queryset.filter(category='1')
        elif value == '2':
            return queryset.filter(category='2')
        else:
            return queryset.none()  # Возвращаем пустой queryset, если значение не "1" или "2"
#пагинация
class PaginationRecipe(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 100

class RecipesAPIList(generics.ListCreateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter
    pagination_class = PaginationRecipe

class RecipesAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAdminOrReadOnly]

class RecipesAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAdminOrReadOnly]

class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecipesFilter
# ml
class SearchRecipeView(APIView):
    def post(self, request):
        user_input = request.data.get('ingredients', [])  # Получаем список ингредиентов из POST-запроса

        matching_recipes = []
        all_recipes = Recipes.objects.all()  # Получаем все рецепты из базы данных

        for recipe in all_recipes:
            recipe_ingredients = eval(recipe.ingr)  # Преобразуем строку в список ингредиентов

            if all(ingredient in user_input for ingredient in recipe_ingredients):
                serializer = RecipeSerializer(recipe)  # Сериализуем найденный рецепт
                matching_recipes.append(serializer.data)

        return Response(matching_recipes)