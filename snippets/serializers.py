from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

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
