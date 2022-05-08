from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProfileModel(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', verbose_name='Картинка профиля')

    def __str__(self):
        return str(self.user)


class Genre(models.Model):
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class BookModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    creator = models.CharField(max_length=100, verbose_name='creator', null=True)
    author = models.CharField(max_length=100, verbose_name='автор')
    contentbook = models.TextField(verbose_name='Содержание')
    picture = models.ImageField(upload_to='images/', verbose_name='Обложка')
    price = models.IntegerField(null=True, verbose_name='Цена')     # Лучше использовать DecimalField
    likes = models.ManyToManyField(User, related_name='book_post', verbose_name='лайкнули')
    genres = models.ManyToManyField(Genre, verbose_name='жанры')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('title',)
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Reviews(models.Model):
    text = models.TextField('Отзыв', max_length=3400)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, null=True, blank=True)
    book = models.ForeignKey(BookModel, verbose_name='книга', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(user=instance)


@receiver
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


def save(self, *args, **kwargs):
    super().save()

    img = Image.open(self.avatar.path)

    if img.height > 100 or img.width > 100:
        new_img = (100, 100)
        img.thumbnail(new_img)
        img.save(self.avatar.path)
