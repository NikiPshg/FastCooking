from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from recipes.views import *


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/recipe/', RecipesAPIList.as_view()),
                  path('api/v1/recipe/<int:pk>/', RecipesAPIUpdate.as_view()),
                  path('api/v1/recipedelete/<int:pk>/', RecipesAPIDestroy.as_view()),
                  path('api/v1/media/recipe_images/', RecipeImageView.as_view(), name='get_image'),
                  path('api/v1/ml_images/', include('ml.urls')),
                  path('api/v1/auth/', include('djoser.urls')),
                  re_path(r'^auth/', include('djoser.urls.authtoken')),
                  path('api/v1/search/', RecipesViewSet.as_view({'get': 'list'}), name='recipes-list'),
                  path('api/v1/search-recipe/', SearchRecipeView.as_view(), name='search_recipe'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
