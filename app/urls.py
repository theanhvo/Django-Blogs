from django.conf.urls import url

from .views import PostListView, PostDetailView, LoginSuccessView

urlpatterns = [
    url(r'^(?P<pk>[-\w]+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^$', PostListView.as_view(), name='post-list'),
    url(r'^login_success$', LoginSuccessView, name='login_success')
]
