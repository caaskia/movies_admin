from rest_framework import serializers
from movies.models import FilmWork, PersonFilmWork, Genre

from django.db.models import prefetch_related_objects


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)

    # Use SerializerMethodField for related persons
    actors = serializers.SerializerMethodField()
    directors = serializers.SerializerMethodField()
    writers = serializers.SerializerMethodField()

    creation_date = serializers.CharField()
    rating = serializers.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        model = FilmWork
        fields = [
            "id",
            "title",
            "description",
            "creation_date",
            "rating",
            "type",
            "genres",
            "actors",
            "directors",
            "writers",
        ]

    # Override to_representation method to include total_pages and prev
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["total_pages"] = self.context.get("total_pages")
        data["prev"] = self.context.get("prev")

        try:
            data["rating"] = float(data.get("rating", 0))
        except (TypeError, ValueError):
            data["rating"] = 0

        return data

    def get_actors(self, obj):
        """
        Get the list of actors for the film work.
        """
        return [
            person.full_name
            for person in obj.persons.filter(personfilmwork__role="actor")
        ]

    def get_directors(self, obj):
        """
        Get the list of directors for the film work.
        """
        return [
            person.full_name
            for person in obj.persons.filter(personfilmwork__role="director")
        ]

    def get_writers(self, obj):
        """
        Get the list of writers for the film work.
        """
        return [
            person.full_name
            for person in obj.persons.filter(personfilmwork__role="writer")
        ]
