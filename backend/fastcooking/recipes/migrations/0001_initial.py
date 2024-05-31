# Generated by Django 5.0.6 on 2024-05-12 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishid', models.CharField(db_index=True, max_length=100)),
                ('namedish', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('nameingr', models.CharField(max_length=255)),
                ('ingr', models.TextField()),
                ('stepname', models.CharField(max_length=255)),
                ('stepdish', models.TextField()),
            ],
        ),
    ]
