from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.db.models import Q

from movies.models import FilmWork


class MoviesListApi(BaseListView):
    model = FilmWork
    http_method_names = ["get"]  # Список методов, которые реализует обработчик

    def get_queryset(self):
        return  # Сформированный QuerySet

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            "results": list(self.get_queryset()),
        }
        return context

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)
