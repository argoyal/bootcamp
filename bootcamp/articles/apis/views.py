from bootcamp.articles.models import Article
from rest_framework.generics import ListAPIView
from .serializers import ArticleSerializer


class APIArticlesListView(ListAPIView):
    """Basic ListView implementation to call the published articles list."""

    serializer_class = ArticleSerializer

    def get_queryset(self, **kwargs):
        return Article.objects.get_published()
