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

    """def create(self, validated_data):
        with open('/var/www/myenv/web/foo.txt', 'w') as f:
            f.write(str(validated_data))
        bookmark_serializer = BookmarkSerializer(data={'bookmark': validated_data['bookmark']})
        if bookmark_serializer.is_valid():
            bookmark_serializer.save()
            bookmark_id = {'bookmark': bookmark_serializer.data['id']}
            data = [dict(item, **bookmark_id) for item in validated_data['urlid']]
            tag_serializer = TagSerializer(data=data, many=True)
            if tag_serializer.is_valid():
                tag_serializer.save()
            else:
                Bookmark.objects.get(bookmark=bookmark_serializer.data['id']).delete()
    """
    class Meta:
        model = Bookmark
        fields = ('bookmark', 'urlid')


class TagToBookmarkSerializer(serializers.ModelSerializer):
    bookmark = BookmarkSerializer()

    class Meta:
        model = Tags
        fields = ('bookmark', 'tag')
