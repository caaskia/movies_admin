from rest_framework import serializers
from movies.models import FilmWork, PersonFilmWork, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class MovieSerializer(serializers.ModelSerializer):
    # genres = GenreSerializer(many=True)
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.SerializerMethodField()
    directors = serializers.SerializerMethodField()
    writers = serializers.SerializerMethodField()

    # Для поля 'creation_date' используется 'CharField', чтобы представить дату как строку
    creation_date = serializers.CharField()

    # Для поля 'rating' используется 'DecimalField', которое соответствует числовому типу данных
    rating = serializers.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        model = FilmWork
        fields = ['id', 'title', 'description', 'creation_date', 'rating', 'type', 'genres', 'actors', 'directors', 'writers']

        # Override to_representation method to include total_pages and prev
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Add total_pages and prev to the response data
        data['total_pages'] = self.context.get('total_pages')
        data['prev'] = self.context.get('prev')

        try:
            data['rating'] = float(data.get('rating', 0))
        except (TypeError, ValueError):
            # Если значение 'rating' не может быть преобразовано в число, установим его в значение по умолчанию
            data['rating'] = 0

        return data

    def get_actors(self, obj):
        return self.get_related_persons(obj, role='actor')

    def get_directors(self, obj):
        return self.get_related_persons(obj, role='director')

    def get_writers(self, obj):
        return self.get_related_persons(obj, role='writer')

    def get_related_persons(self, film_work, role):
        person_filmworks = PersonFilmWork.objects.select_related('person').filter(film_work=film_work, role=role)
        return [person_filmwork.person.full_name for person_filmwork in person_filmworks]