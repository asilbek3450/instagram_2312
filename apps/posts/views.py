from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from .models import Post, PostImage, PostLike, Comment, CommentReply, CommentLike, CommentReplyLike
from .serializers import PostSerializer, CommentSerializer, CommentReplySerializer
from rest_framework.decorators import action


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        post_like, created = PostLike.objects.get_or_create(user=user, post=post)
        if created:
            return Response({'status': 'like added'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        try:
            post_like = PostLike.objects.get(user=user, post=post)
            post_like.delete()
            return Response({'status': 'like removed'}, status=status.HTTP_204_NO_CONTENT)
        except PostLike.DoesNotExist:
            return Response({'status': 'not liked yet'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def comment(self, request, pk=None):
        post = self.get_object()
        content = request.data.get('content')
        if content:
            comment = Comment.objects.create(user=request.user, post=post, content=content)
            return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Content is required'}, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        comment_like, created = CommentLike.objects.get_or_create(user=user, comment=comment)
        if created:
            return Response({'status': 'like added'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def unlike(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        try:
            comment_like = CommentLike.objects.get(user=user, comment=comment)
            comment_like.delete()
            return Response({'status': 'like removed'}, status=status.HTTP_204_NO_CONTENT)
        except CommentLike.DoesNotExist:
            return Response({'status': 'not liked yet'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def reply(self, request, pk=None):
        comment = self.get_object()
        content = request.data.get('content')
        if content:
            reply = CommentReply.objects.create(user=request.user, comment=comment, content=content)
            return Response(CommentReplySerializer(reply).data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Content is required'}, status=status.HTTP_400_BAD_REQUEST)


class CommentReplyViewSet(viewsets.ModelViewSet):
    queryset = CommentReply.objects.all()
    serializer_class = CommentReplySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])  # dekorator to add like functionality
    def like(self, request, pk=None):
        comment_reply = self.get_object()
        user = request.user
        reply_like, created = CommentReplyLike.objects.get_or_create(user=user, comment_reply=comment_reply)
        if created:
            return Response({'status': 'like added'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def unlike(self, request, pk=None):
        comment_reply = self.get_object()
        user = request.user
        try:
            reply_like = CommentReplyLike.objects.get(user=user, comment_reply=comment_reply)
            reply_like.delete()
            return Response({'status': 'like removed'}, status=status.HTTP_204_NO_CONTENT)
        except CommentReplyLike.DoesNotExist:
            return Response({'status': 'not liked yet'}, status=status.HTTP_400_BAD_REQUEST)
