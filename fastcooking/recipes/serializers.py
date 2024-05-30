from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Recipes, Image

class RecipeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"



class RecipeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Recipes
        fields = "__all__"


class RecipeSerializerML(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = "__all__"