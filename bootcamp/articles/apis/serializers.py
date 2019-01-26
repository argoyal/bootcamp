from rest_framework import serializers
from bootcamp.articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer class for listing the articles
    """

    popular_tags = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    def get_popular_tags(self, obj):
        return Article.objects.get_counted_tags()

    def get_tags(self, obj):
        return [tag for tag in obj.tags.names()]

    class Meta:
        model = Article
        fields = ["title", "content", "image", "tags", "status", "edited",
                  "popular_tags"]
