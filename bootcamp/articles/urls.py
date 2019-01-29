from django.conf.urls import url

from bootcamp.articles.views import (ArticlesListView, DraftsListView,
                                     CreateArticleView, EditArticleView,
                                     DetailArticleView)
from bootcamp.articles.apis.views import APIArticlesListView, \
    APIDraftsListView, APICreateArticleView, APIUpdateArticleView


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
    url(r'^api/drafts/$', APIDraftsListView.as_view(), name='list_drafts'),
    url(r'^api/articles/new/$', APICreateArticleView.as_view(),
        name='create_articles'),
    url(r'^api/articles/update/(?P<pk>\d+)/$', APIUpdateArticleView.as_view(),
        name='update_articles'),
]


urlpatterns = view_urls + api_urls
