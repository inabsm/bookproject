from django.contrib import admin

from .models import BookModel, ProfileModel, Reviews, Genre


class BookModelAdmin(admin.ModelAdmin):
    pass


class ProfileModelAdmin(admin.ModelAdmin):
    pass


class ReviewsAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Genre, GenreAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(ProfileModel, ProfileModelAdmin)
admin.site.register(BookModel, BookModelAdmin)
