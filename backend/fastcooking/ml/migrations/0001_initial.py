# Generated by Django 5.0.6 on 2024-05-18 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MlImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ml_images')),
                ('result', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
