from django.conf.urls import url
from bootcamp.articles.apis.views import APIArticlesListView, \
    APIDraftsListView, APICreateArticleView, APIUpdateArticleView


urlpatterns = [
    url(r'^$', APIArticlesListView.as_view(), name='list_articles'),
    url(r'^drafts/$', APIDraftsListView.as_view(), name='list_drafts'),
    url(r'^articles/new/$', APICreateArticleView.as_view(),
        name='create_articles'),
    url(r'^articles/update/(?P<pk>\d+)/$', APIUpdateArticleView.as_view(),
        name='update_articles'),
]
