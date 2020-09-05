from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
    """
    Entrypoint
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

class SnippetHighlight(generics.GenericAPIView):
    """
    Shows highlight
    """
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        """
        GET method
        """
        snippet = self.get_object()
        return Response(snippet.highlighted)

class SnippetList(generics.ListCreateAPIView):
    """
    List of snippets
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View, Modify or delete specific snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    """
    User list view
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserDetail(generics.RetrieveAPIView):
    """
    User detail
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
