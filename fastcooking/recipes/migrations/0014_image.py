# Generated by Django 5.0.6 on 2024-05-15 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_delete_recipeimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('dish', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='recipes.recipes')),
                ('image', models.ImageField(upload_to='recipe_images/')),
            ],
        ),
    ]
