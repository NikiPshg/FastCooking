# myapp/urls.py
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
                  path('urls/',RecipeURLView.as_view()),
                  path('recipe/', RecipesAPIList.as_view()),
                  path('recipe/<int:pk>/', RecipesAPIUpdate.as_view()),
                  path('recipedelete/<int:pk>/', RecipesAPIDestroy.as_view()),
                  path('media/recipe_images/', RecipeImageView.as_view(), name='get_image'),
                  path('search/', RecipesViewSet.as_view({'get': 'list'}), name='recipes-list'),
              ]
