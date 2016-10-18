from django.conf.urls import url

from posts.views import PostView


urlpatterns = [
    url(r'^', PostView.as_view())
]