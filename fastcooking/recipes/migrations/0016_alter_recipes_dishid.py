# Generated by Django 5.0.6 on 2024-05-15 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_alter_recipes_dishid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='dishid',
            field=models.IntegerField(db_index=True, primary_key=True, serialize=False),
        ),
    ]