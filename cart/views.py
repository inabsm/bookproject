from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from bookapp.models import *
from .cart import Cart
from .forms import CardAddBookForm


@require_POST
def cart_add(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(BookModel, id=book_id)
    form = CardAddBookForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book=book,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(BookModel, id=book_id)
    cart.remove(book)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CardAddBookForm(
            initial={'quantity': item['quantity'],
                     'update': True}
        )

    return render(request, 'cart/detail.html', context={'cart': cart})
