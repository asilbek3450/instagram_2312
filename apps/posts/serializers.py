from rest_framework import serializers
from .models import Post, PostImage, PostLike, Comment, CommentReply, CommentLike, CommentReplyLike


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image']


class CommentLikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = CommentLike
        fields = ['id', 'user', 'created_at']


class CommentReplyLikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = CommentReplyLike
        fields = ['id', 'user', 'created_at']


class CommentReplySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = CommentReply
        fields = ['id', 'user', 'content', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    replies = CommentReplySerializer(many=True, read_only=True)
    likes = CommentLikeSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'content', 'created_at', 'replies', 'likes']


class PostLikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = PostLike
        fields = ['id', 'user', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    images = PostImageSerializer(many=True, read_only=True)
    likes = PostLikeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'text', 'created_at', 'images', 'likes', 'comments']
