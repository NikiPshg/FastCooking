from django.contrib.auth.models import User
from django.db import models


class Recipes(models.Model):
    dishid = models.CharField(max_length=100, db_index=True)  # ключ для картинок
    namedish = models.CharField(max_length=255)  # Заголовок рецепта
    description = models.TextField()  # Описание
    nameingr = models.CharField(max_length=255)  # Заголовок ингредиентов
    ingr = models.TextField()  # Список ингредиентов
    stepname = models.CharField(max_length=255)  # Подзаголовок рецепта (к названию просто добавилось слово рецепт)
    stepdish = models.TextField()  # Пошаговое приготовление
    category = models.CharField(max_length=1) # категория

    def __str__(self):
        return self.namedish

class Filter(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

# class Image(models.Model):
#     dishid = models.ForeignKey('Recipes', on_delete=models.PROTECT, null=True)
#