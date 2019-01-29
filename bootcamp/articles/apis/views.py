from bootcamp.articles.models import Article
from rest_framework.generics import ListAPIView, CreateAPIView, \
    UpdateAPIView
from rest_framework.parsers import MultiPartParser
from .serializers import ArticleSerializer


class APIArticlesListView(ListAPIView):
    """Basic ListView implementation to call the published articles list."""

    serializer_class = ArticleSerializer

    def get_queryset(self, **kwargs):
        return Article.objects.get_published()


class APIDraftsListView(ListAPIView):
    """Overriding the original implementation to call the drafts articles
    list."""

    serializer_class = ArticleSerializer

    def get_queryset(self, **kwargs):
        return Article.objects.get_drafts()


class APICreateArticleView(CreateAPIView):
    """Basic CreateView implementation to create new articles."""

    serializer_class = ArticleSerializer
    parser_classes = (MultiPartParser, )


class APIUpdateArticleView(UpdateAPIView):
    """Basic EditView implementation to edit existing articles."""

    serializer_class = ArticleSerializer
    parser_classes = (MultiPartParser, )

    def get_queryset(self, **kwargs):
        return Article.objects.filter(id=int(self.kwargs.get('pk')))
