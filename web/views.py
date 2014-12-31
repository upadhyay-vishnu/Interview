# Create your views here.
from django.http import Http404

from rest_framework.views import APIView, status
from rest_framework.response import Response

from .serializers import BookmarkSerializer, TagSerializer
from .models import Bookmark, Tags


class Insert_URL(APIView):
    """
    inserting the Bookmark
    """

    def post(self, request):
        #bookmark_serializer = BookmarkSerializer(data=request.data)
        bookmark_serializer = BookmarkSerializer(data={'bookmark': request.data['bookmark']})
        if bookmark_serializer.is_valid():
            bookmark_serializer.save()
            bookmark_id = {'bookmark': bookmark_serializer.data['id']}
            bkid = Bookmark.objects.get(id=bookmark_id['bookmark'])
            bkid.url_tag.add(*([Tags.objects.create(tag=tag['tag']) for tag in request.data['urlid']]))
            serializer = TagSerializer(bkid.url_tag.all(), many=True)
            return Response('created', status=status.HTTP_201_CREATED)
        return Response(bookmark_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #return Response(bookmark.data, status=status.HTTP_200_OK)


class Url_Detail_Update(APIView):
    """
    Delete The Existing URL
    """

    def get_object(self, pk):
        try:
            return Bookmark.objects.get(pk=pk)
        except Bookmark.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Return All Relateg Tgas To The URL
        """
        data = {'tags': []}
        url = self.get_object(pk=pk)
        serializer = TagSerializer(url.url_tag.all(), many=True)
        data['Url'] = url.bookmark
        for item in serializer.data:
            data['tags'].append(item['tag'])
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        data = {'tags': []}
        url = self.get_object(pk=pk)
        try:
            for tag in request.data['tags']:
                _tag = Tags.objects.get(tag=tag)
                url.url_tag.add(_tag)
        except Tags.DoesNotExist as e:
            return Response(e.message, status=status.HTTP_404_NOT_FOUND)
        serializer = TagSerializer(url.url_tag.all(), many=True)
        data['Url'] = url.bookmark
        for item in serializer.data:
            data['tags'].append(item['tag'])
        return Response(data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk, format=None):
        bookmark = self.get_object(pk=pk)
        bookmark.delete()
        return Response(status=status.HTTP_302_FOUND)


class Edit_URL(APIView):
    """
    Editting the URL by adding or updating tags
    """

    def put(self, request, pk, format=None):
        data = {'tags': []}
        url = Url_Detail_Update().get_object(pk=pk)
        try:
            for tag in request.data['tags']:
                _tag = Tags.objects.get(tag=tag)
                url.url_tag.add(_tag)
        except Tags.DoesNotExist as e:
            return Response(e.message, status=status.HTTP_404_NOT_FOUND)
        serializer = TagSerializer(url.url_tag.all(), many=True)
        data['Url'] = url.bookmark
        for item in serializer.data:
            data['tags'].append(item['tag'])
        return Response(data, status.HTTP_201_CREATED)


class Tag_Detail_Upadte(APIView):
    """
    Editting and Returning the detail of TagSerializer
    """
    def get_object(self, pk):
        try:
            return Tags.objects.get(pk=pk)
        except Tags.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        """
        Get all URL related to The Tag
        """
        data = {}
        tag = self.get_object(pk=pk)
        #tags = tag.bookmark.all()
        serializer = BookmarkSerializer(tag.bookmark.all(), many=True)
        data['bookmarks'] = serializer.data
        data['tag'] = tag.tag
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        tag = self.get_object(pk=pk)
        serializer = TagSerializer(tag, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tag = self.get_object(pk)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Edit_Tag(APIView):
    """
    Editting the Tag
    """
    def put(self, request, pk, format=None):
        tag = Tag_Detail_Upadte().get_object(pk=pk)
        serializer = TagSerializer(tag, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Create_Tag(APIView):
    """
    Generate New Tag
    """

    def create_object(self, request):
        tag = Tags(tag=request.data['tag'])
        if tag.tag.strip() != '':
            tag.save()
            return tag
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        data = {'Name': ''}
        tag = self.create_object(request)
        data['Name'] = tag.tag
        data['message'] = "Tag was successfully created"
        return Response(data, status=status.HTTP_201_CREATED)


class UrlList(APIView):

    def get_object(self, pk):
        try:
            return Bookmark.objects.get(pk=pk)
        except Bookmark.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        """
        Update the existing tags for URLs
        """
        bookmark = self.get_object(pk)
        serializer = TagSerializer(bookmark, data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
