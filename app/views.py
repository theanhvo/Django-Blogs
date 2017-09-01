
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
from django.http import HttpResponse

from .models import Blog


class PostListView(ListView):

    model = Blog
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PostDetailView(DetailView):

    model = Blog

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def LoginSuccessView(request):
    return HttpResponse('FB Login OK')
