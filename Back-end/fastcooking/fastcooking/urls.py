from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from recipes.views import *
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/',include('recipes.urls')),
                  path('api/v1/ml_images/', include('ml.urls')),
                  path('api/v1/auth/', include('djoser.urls')),
                  re_path(r'^auth/', include('djoser.urls.authtoken')),
                  path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
                  path(
                        '',
                        SpectacularSwaggerView.as_view(url_name='api-schema'),
                        name='api-docs',
                    ),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
