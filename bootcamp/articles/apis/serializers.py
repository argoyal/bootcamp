from rest_framework import serializers
from bootcamp.articles.models import Article
from bootcamp.api_mixins import CommonAPIMixin


class ArticleSerializer(CommonAPIMixin, serializers.ModelSerializer):
    """
    Serializer class for listing the articles
    """

    popular_tags = serializers.SerializerMethodField()
    image = serializers.ImageField(required=False)

    def get_popular_tags(self, obj):
        return Article.objects.get_counted_tags()

    class Meta:
        model = Article
        fields = ["title", "content", "image", "tags", "status", "edited",
                  "popular_tags", "user", "user_name"]

    def to_representation(self, instance):
        ret_dict = super(ArticleSerializer, self).to_representation(instance)

        if type(instance) == self.Meta.model:
            ret_dict['tags'] = [tag for tag in instance.tags.names()]

        return ret_dict

    def create(self, validated_data):
        validated_data['user'] = self.user

        return super(ArticleSerializer, self).create(validated_data)
