# Generated by Django 4.2.3 on 2023-08-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieCatalogApp', '0002_movie_cover_image_movie_trailer_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.CharField(max_length=50),
        ),
    ]