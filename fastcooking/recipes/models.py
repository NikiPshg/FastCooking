from django.contrib.auth.models import User
from django.db import models



# class ImageAPI(models.Model):
#     name = models.CharField(max_length=100, primary_key=True)
#     image = models.ImageField(upload_to='images/')
#

class Recipes(models.Model):
    dishid = models.IntegerField( db_index=True, primary_key=True)  # ключ для картинок
    #dishid = models.ForeignKey(ImageAPI, on_delete=models.CASCADE)
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

class Image(models.Model):
    dish = models.OneToOneField(Recipes, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='recipe_images/')


# class ImageFile(models.Model):
#     image = models.ImageField(upload_to='images/')
#     image_key = models.ForeignKey(Recipes, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.image_key.dishid