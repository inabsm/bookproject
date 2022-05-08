from django import forms
from django.contrib.auth.models import User

from .models import BookModel, ProfileModel, Reviews



class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['title', 'author', 'contentbook', 'picture', 'price', 'genres']


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Подтвердите пароль')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    email = forms.EmailField(required=True, label='Почта')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        labels = {
            'username': 'Логин'
        }


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    class Meta:
        fields = ['username', 'password']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)

    class Meta:
        fields = ['avatar']
        model = ProfileModel


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ("text",)
