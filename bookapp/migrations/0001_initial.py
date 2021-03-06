# Generated by Django 4.0.2 on 2022-04-24 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='default.jpg', upload_to='', verbose_name='Картинка профиля')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('creator', models.CharField(max_length=100, null=True, verbose_name='creator')),
                ('author', models.CharField(max_length=100, verbose_name='автор')),
                ('contentbook', models.TextField(verbose_name='Содержание')),
                ('picture', models.ImageField(upload_to='images/', verbose_name='Обложка')),
                ('price', models.IntegerField(null=True, verbose_name='Цена')),
                ('price_rent', models.IntegerField(null=True, verbose_name='Аренда')),
                ('likes', models.ManyToManyField(related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
