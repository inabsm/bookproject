import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, CreateView

from cart.forms import *
from .forms import *
from .models import *


def index(request):
    return render(request, 'bookapp/index.html')


def allbook(request):
    allbook = BookModel.objects.all()
    cart_book_form = CardAddBookForm()
    return render(request, 'bookapp/bookmodel_list.html', context={
        'allbook': allbook,
        'cart_book_form': cart_book_form

    })


class GenreView:

    def get_genres(self):
        return Genre.objects.all()


class AddBookView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'bookapp/addbook.html', context={'form': form})

    def post(self, request):
        form = BookForm()
        if request.method == 'POST':
            form = BookForm(request.POST or None, request.FILES)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.creator = request.user.username
                new_post.save()
                form.save()
                return redirect('allbook')
        return render(request, 'bookapp/addbook.html', context={
            'form': form
        })


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'bookapp/register.html'
    success_url = 'login'


class MyLoginView(LoginRequiredMixin, LoginView):
    redirect_authenticated_user = True
    template_name = 'bookapp/login.html'
    login_url = '/login/'


class MoreInfoView(View):
    """Вывод данных на страницу 'подробнее' """

    def get(self, request, id):
        book_cart = get_object_or_404(BookModel, id=id)
        book_info = BookModel.objects.filter(id=id).first()
        cart_book_form = CardAddBookForm()
        stuff = get_object_or_404(BookModel, id=self.kwargs['id'])
        total_likes = stuff.total_likes()
        return render(request, 'bookapp/more_info.html', context={
            'id': id,
            'book_info': book_info,
            'book': BookModel.objects.all(),
            'total_likes': total_likes,
            'book_cart': book_cart,
            'cart_book_form': cart_book_form
        })


class AddReview(View):
    """Добавления отзывов"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        user = request.user
        book = BookModel.objects.get(id=pk)
        if not request.user.is_authenticated:
            raise PermissionDenied()
        if form.is_valid():
            form = form.save(commit=False)
            form.book = book
            form.user = user
            form.save()
        return HttpResponseRedirect(reverse('more_info', args=[pk]))


def LikeView(request, pk):
    """лайки"""
    book = BookModel.objects.get(id=pk)

    user = request.user
    if user in book.likes.all():
        book.likes.remove(request.user)
    else:
        book.likes.add(request.user)
    return HttpResponseRedirect(reverse('more_info', args=[pk]))


def random_book(request):
    """Случайная книга"""
    book_pks = list(BookModel.objects.values_list('pk', flat=True))
    pk = random.choice(book_pks)
    book_random = get_object_or_404(BookModel, pk=pk)
    return render(request, 'bookapp/random.html', context={'book_random': book_random})


@login_required
def profileview(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profilemodel)

        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('profile')
    else:
        form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm()

    return render(request, 'bookapp/profile.html', context={
        'form': form,
        'profile_form': profile_form
    })


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'bookapp/change_password.html'
    success_message = 'Success'
    success_url = reverse_lazy('profile')
