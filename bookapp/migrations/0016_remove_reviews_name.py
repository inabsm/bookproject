# Generated by Django 4.0.2 on 2022-05-01 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0015_rename_name_user_reviews_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='name',
        ),
    ]
