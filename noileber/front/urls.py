from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^noticias/(?P<article_id>\d+)/(?P<article_slug>[\w-]+)', views.article, name='article'),
    url(r'^categoria/(?P<category_slug>[\w-]+)', views.category, name='category'),
]
