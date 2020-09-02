from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        """
        Show snippet list
        """
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create new snippet
        """
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, snippet_id):
        """
        Helper to get object
        """
        try:
            return Snippet.objects.get(pk=snippet_id)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, snippet_id, format=None):
        """
        Show object
        """
        snippet = self.get_object(snippet_id)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, snippet_id, format=None):
        """
        Modify object
        """
        snippet = self.get_object(snippet_id)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, snippet_id, format=None):
        """
        Remove object
        """
        snippet = self.get_object(snippet_id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
