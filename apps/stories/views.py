from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Story, StoryLike, StoryView
from .serializers import StorySerializer, StoryLikeSerializer, StoryViewSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        story = self.get_object()
        user = request.user
        StoryLike.objects.create(user=user, story=story)
        return Response({'status': 'liked'})

    @action(detail=True, methods=['post'])
    def view(self, request, pk=None):
        story = self.get_object()
        user = request.user
        StoryView.objects.create(user=user, story=story)
        return Response({'status': 'viewed'})


class StoryLikeViewSet(viewsets.ModelViewSet):
    queryset = StoryLike.objects.all()
    serializer_class = StoryLikeSerializer


class StoryViewViewSet(viewsets.ModelViewSet):
    queryset = StoryView.objects.all()
    serializer_class = StoryViewSerializer
    permission_classes = [IsAuthenticated]

    # Only authenticated users can view the story views
    def get_queryset(self):
        return self.queryset.filter(story__user=self.request.user)
