# Generated by Django 4.0.2 on 2022-05-01 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0017_remove_genre_url_bookmodel_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='url',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
