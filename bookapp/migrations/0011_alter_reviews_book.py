# Generated by Django 4.0.2 on 2022-04-30 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0010_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.bookmodel', verbose_name='книга'),
        ),
    ]
