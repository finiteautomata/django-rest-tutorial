from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Snippet

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Snippet class
    """
    class Meta:
        model = Snippet
        fields = [
            'url', 'id', 'highlight', 'owner',
            'title', 'code', 'linenos', 'language', 'style'
        ]

    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name="snippet-highlight", format="html")

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User class
    """
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name="snippet-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
