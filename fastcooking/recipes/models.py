from django.contrib.auth.models import User
from django.db import models


# модель рецептов
class Recipes(models.Model):
    dishid = models.IntegerField(db_index=True, primary_key=True)  # ключ для картинок
    namedish = models.CharField(max_length=255)  # Заголовок рецепта
    description = models.TextField()  # Описание
    nameingr = models.CharField(max_length=255)  # Заголовок ингредиентов
    ingr = models.TextField()  # Список ингредиентов
    stepname = models.CharField(max_length=255)  # Подзаголовок рецепта (к названию просто добавилось слово рецепт)
    stepdish = models.TextField()  # Пошаговое приготовление
    category = models.CharField(max_length=1)  # категория
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)  # юзер

    def __str__(self):
        return self.namedish


# модель фильтра
class Filter(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


# модель изображений
class Image(models.Model):
    dish = models.OneToOneField(Recipes, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='recipe_images/')
