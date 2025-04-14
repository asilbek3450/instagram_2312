from rest_framework import serializers
from .models import Story, StoryLike, StoryView


class StorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Foydalanuvchi nomi
    story_views = serializers.StringRelatedField(many=True)  # Foydalanuvchilarni ko'rgan

    class Meta:
        model = Story
        fields = ['id', 'user', 'image', 'created_at', 'expires_at', 'story_views']


class StoryLikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Foydalanuvchi nomi
    story = serializers.StringRelatedField()  # Hikoya

    class Meta:
        model = StoryLike
        fields = ['user', 'story', 'created_at']


class StoryViewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Foydalanuvchi nomi
    story = serializers.StringRelatedField()  # Hikoya

    class Meta:
        model = StoryView
        fields = ['user', 'story', 'viewed_at']
