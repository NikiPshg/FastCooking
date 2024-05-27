# myapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from inference_sdk import InferenceHTTPClient
import tempfile
from PIL import Image


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
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
