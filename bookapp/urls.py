from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from bookapp import views

urlpatterns = [
    path('', index, name='index'),
    path('allbook', allbook, name='allbook'),
    path('addbook', AddBookView.as_view(), name='addbook'),
    path('register', RegisterView.as_view(), name='reg'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('book/<int:id>', MoreInfoView.as_view(), name='more_info'),
    path('profile', profileview, name='profile'),
    path('password-change', ChangePasswordView.as_view(), name='change_pass'),
    path('like/<int:pk>', LikeView, name='like_book'),
    path('random/', views.random_book, name='random_book'),
    path('review/<int:pk>', AddReview.as_view(), name='review'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)