from django.shortcuts import render
from .models import Recipes
from rest_framework import generics
from .serializers import RecipeSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated

class RecipesAPIList(generics.ListCreateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

class RecipesAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAdminOrReadOnly]

class RecipesAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAdminOrReadOnly]

