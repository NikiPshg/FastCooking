# myapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from inference_sdk import InferenceHTTPClient
import tempfile
from recipes.models import Recipes  # Импортируем модель
from recipes.serializers import RecipeSerializerML  # Импортируем сериализатор
from googletrans import Translator
from collections import Counter



class PredictView(APIView):
    def post(self, request):
        file = request.FILES['image']

        # Сохранение загруженного изображения во временный файл
        with tempfile.NamedTemporaryFile(delete=False) as temp_image:
            for chunk in file.chunks():
                temp_image.write(chunk)
            temp_image_path = temp_image.name

        # Инициализация клиента
        client = InferenceHTTPClient(
            api_url=settings.ROBOFLOW_API_URL,
            api_key=settings.ROBOFLOW_API_KEY
        )

        # Предсказание
        try:
            result = client.infer(temp_image_path, model_id="eat-69w8e/3")

            # Извлечение уникальных классов из предсказаний
            unique_classes = list(set(prediction['class'] for prediction in result['predictions']))

            # Перевод уникальных классов на русский
            translator = Translator()
            translated_classes = [translator.translate(cls, src='en', dest='ru').text.capitalize() for cls in
                                  unique_classes]

            # Поиск рецептов, которые содержат все совпадающие ингредиенты
            matching_recipes = []
            for recipe in Recipes.objects.all():
                recipe_ingredients = eval(recipe.ingr)
                matching_count = sum(ingredient in translated_classes for ingredient in recipe_ingredients)
                if len(recipe_ingredients) - matching_count <= 1:
                    matching_recipes.append(recipe)

            # Сериализация рецептов для ответа
            serialized_recipes = RecipeSerializerML(matching_recipes, many=True)

            return Response({"classes": translated_classes, "matching_recipes": serialized_recipes.data},
                            # после убрать translated_classes
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # # выводит классы
        # try:
        #     result = client.infer(temp_image_path, model_id="eat-69w8e/3")
        #
        #     # Извлечение уникальных классов из предсказаний
        #     unique_classes = list(set(prediction['class'] for prediction in result['predictions']))
        #
        #     # Перевод уникальных классов на русский
        #     translator = Translator()
        #     translated_classes = [translator.translate(cls, src='en', dest='ru').text for cls in unique_classes]
        #
        #     return Response({"classes": translated_classes}, status=status.HTTP_200_OK)
        # except Exception as e:
        #     return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
