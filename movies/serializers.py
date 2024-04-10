from rest_framework import serializers
from movies.models import FilmWork


class MovieSerializer(serializers.ModelSerializer):
    # genres = serializers.StringRelatedField(many=True)
    genres = serializers.SerializerMethodField()

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

    def get_genres(self, obj):
        genres_qs = obj.genrefilmwork.all()
        return [genrefilmwork.genre.name for genrefilmwork in genres_qs]

    def get_actors(self, obj):
        persons_qs = obj.personfilmwork.all()
        return self.get_persons_by_role(persons_qs, "actor")

    def get_directors(self, obj):
        persons_qs = obj.personfilmwork.all()
        return self.get_persons_by_role(persons_qs, "director")

    def get_writers(self, obj):
        persons_qs = obj.personfilmwork.all()
        return self.get_persons_by_role(persons_qs, "writer")

    def get_persons_by_role(self, persons_qs, role):
        return [
            person_filmwork.person.full_name
            for person_filmwork in persons_qs
            if person_filmwork.role == role
        ]
