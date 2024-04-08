from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView
from movies.models import FilmWork
from django.core.paginator import Paginator


class MoviesApiMixin:
    model = FilmWork
    http_method_names = ["get"]

    def get_queryset(self):
        return self.model.objects.all()

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        paginator = Paginator(queryset, 50)  # Paginate queryset with 50 elements per page
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        
        context = {
            "count": paginator.count,
            "total_pages": paginator.num_pages,
            "prev": page_obj.previous_page_number() if page_obj.has_previous() else None,
            "next": page_obj.next_page_number() if page_obj.has_next() else None,
            "results": list(page_obj.object_list.values()),  # Convert QuerySet to list of dictionaries
        }
        return self.render_to_response(context)


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    def get_context_data(self, **kwargs):
        obj = self.get_object()
        context = obj.__dict__  # Convert model object to dictionary
        return context
