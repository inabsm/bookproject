# Generated by Django 4.0.2 on 2022-05-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0020_remove_bookmodel_url_remove_genre_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True, verbose_name='Slug'),
        ),
    ]
