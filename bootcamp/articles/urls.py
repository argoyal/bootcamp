from django.conf.urls import url

from bootcamp.articles.views import (ArticlesListView, DraftsListView,
                                     CreateArticleView, EditArticleView,
                                     DetailArticleView)
from bootcamp.articles.apis.views import APIArticlesListView

app_name = 'articles'

view_urls = [
    url(r'^$', ArticlesListView.as_view(), name='list'),
    url(r'^write-new-article/$', CreateArticleView.as_view(), name='write_new'),
    url(r'^drafts/$', DraftsListView.as_view(), name='drafts'),
    url(r'^edit/(?P<pk>\d+)/$', EditArticleView.as_view(), name='edit_article'),
    url(r'^(?P<slug>[-\w]+)/$', DetailArticleView.as_view(), name='article'),
]

api_urls = [
    url(r'^api/articles/$', APIArticlesListView.as_view(), name='list_articles'),
]


urlpatterns = view_urls + api_urls
