# Generated by Django 4.0.2 on 2022-05-05 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0023_alter_genre_options_genre_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmodel',
            options={'ordering': ('title',), 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]
