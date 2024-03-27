from django.db.models.functions import Lower
from django.utils.translation import gettext_lazy as _

from django.contrib import admin

from .models import Genre, FilmWork, Person, PersonFilmWork, GenreFilmWork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    list_filter = ('full_name',)
    search_fields = ('full_name',)


@admin.register(PersonFilmWork)
class PersonFilmWorkAdmin(admin.ModelAdmin):
    list_display = ('film_work', 'person', 'role')
    list_filter = ('person', 'role',)
    search_fields = ('film_work', 'person', 'role')
    autocomplete_fields = ['person']


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmWork
    verbose_name_plural = 'Жанры фильма'
    verbose_name = 'Жанр фильма'
    extra = 1
    autocomplete_fields = ['genre']

class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmWork
    extra = 1
    autocomplete_fields = ['person']

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')


@admin.register(FilmWork)
class FilmworkAdmin(admin.ModelAdmin):
    def get_ordering(self, request):
        if request.GET.get('o') is None:
            return [Lower('title')]  # sort case insensitive
        else:
            return super().get_ordering(request)

    verbose_name = _('Film work')
    verbose_name_plural = _('Film works')
    inlines = (GenreFilmworkInline, PersonFilmworkInline,)

    # Отображение полей в списке
    list_display = ('title', 'type', 'creation_date', 'rating', 'created', 'modified')

    # Сортировка по умолчанию
    ordering = ('title', 'type')

    # Фильтрация в списке
    list_filter = ('type', 'genres', 'rating', )

    # Поиск по полям
    search_fields = ('title', 'description', 'id')











