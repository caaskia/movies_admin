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
        return self.get_persons_by_role(obj, "actor")

    def get_directors(self, obj):
        return self.get_persons_by_role(obj, "director")

    def get_writers(self, obj):
        return self.get_persons_by_role(obj, "writer")

    def get_persons_by_role(self, obj, role):
        persons = obj.filmwork.filter(role=role)
        return [person.person.full_name for person in persons]


#  def get_related_persons(self, persons_qs, role):
#     return [
#         person.full_name
#         for person in persons_qs
#         if person.personfilmwork.filter(role=role).exists()
#     ]

#        return self.get_related_persons(obj.persons.all(), "actor")
#       return self.get_related_persons(obj.persons.all(), "director")
#       return self.get_related_persons(obj.persons.all(), "writer")
