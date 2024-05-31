from django.contrib import admin

from .models import Recipes, Image

# Register your models here.
admin.site.register(Recipes)
admin.site.register(Image)