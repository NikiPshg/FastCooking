from django.contrib import admin
from django.urls import path,include,re_path
from recipes.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/recipe/', RecipesAPIList.as_view()),
    path('api/v1/recipe/<int:pk>/', RecipesAPIUpdate.as_view()),
    path('api/v1/recipedelete/<int:pk>/', RecipesAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')), 
    re_path(r'^search/', RecipeModelListView.as_view(), name='recipemodel-list'),
]

#сделать фильтр овощи,мясо,рыба

