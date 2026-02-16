from rest_framework import serializers
from .models import Post, Comment

# Comment serializer
class CommentSerializer(serializers.ModelSerializer):
    # Show author username as read-only
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

# Post serializer
class PostSerializer(serializers.ModelSerializer):
    # Show author username as read-only
    author = serializers.ReadOnlyField(source='author.username')
    # Include comments count
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content',
                 'created_at', 'updated_at', 'comments_count']
        read_only_fields = ['author', 'created_at', 'updated_at']

    def get_comments_count(self, obj):
        return obj.comments.count()
