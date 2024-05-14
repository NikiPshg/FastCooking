from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Recipes
from rest_framework import generics
from .serializers import RecipeSerializer
from .permissions import *
from rest_framework.pagination import PageNumberPagination
from django.views.generic import ListView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import ObjectDoesNotExist

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
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter

class RecipesAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryFilter

class RecipeModelListView(generics.ListAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
    filter_class = RecipeModelFilter




