from rest_framework import serializers
from movies.models import FilmWork, PersonFilmWork, Genre


# class FilmWorkSerializer(serializers.ModelSerializer):

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.SerializerMethodField()
    directors = serializers.SerializerMethodField()
    writers = serializers.SerializerMethodField()
    genres = GenreSerializer(many=True)

    class Meta:
        model = FilmWork
        fields = ['id', 'title', 'description', 'creation_date', 'rating', 'type', 'genres', 'actors', 'directors', 'writers']

    def get_actors(self, obj):
        person_filmworks = PersonFilmWork.objects.filter(film_work=obj, role='actor')
        actors = [person_filmwork.person.full_name for person_filmwork in person_filmworks]
        return actors

    def get_directors(self, obj):
        person_filmworks = PersonFilmWork.objects.filter(film_work=obj, role='director')
        directors = [person_filmwork.person.full_name for person_filmwork in person_filmworks]
        return directors

    def get_writers(self, obj):
        person_filmworks = PersonFilmWork.objects.filter(film_work=obj, role='writer')
        writers = [person_filmwork.person.full_name for person_filmwork in person_filmworks]
        return writers