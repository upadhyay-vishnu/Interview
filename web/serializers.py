from rest_framework import serializers
from .models import Bookmark, Tags


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = ('tag', 'bookmark')


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id', 'bookmark',)


class BookmarkWithTagSerializer(serializers.ModelSerializer):
    urlid = TagSerializer(many=True)

    class Meta:
        model = Bookmark
        fields = ('bookmark', 'urlid')


class TagToBookmarkSerializer(serializers.ModelSerializer):
    bookmark = BookmarkSerializer()

    class Meta:
        model = Tags
        fields = ('bookmark', 'tag')
