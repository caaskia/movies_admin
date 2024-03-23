from django.contrib import admin

from .models import Genre, FilmWork, Person, PersonFilmWork, GenreFilmWork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(FilmWork)
class FilmWorkAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(PersonFilmWork)
class PersonFilmWorkAdmin(admin.ModelAdmin):
    pass


@admin.register(GenreFilmWork)
class GenreFilmWorkAdmin(admin.ModelAdmin):
    pass


