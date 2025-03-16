from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Count
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'])
    def most_liked(self, request):
        """Получить посты, отсортированные по количеству лайков"""
        posts = Post.objects.annotate(likes_count=Count('likes')).order_by('-likes_count')[:5]
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def most_commented(self, request):
        """Получить посты, отсортированные по количеству комментариев"""
        posts = Post.objects.annotate(comments_count=Count('comments')).order_by('-comments_count')[:5]
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def toggle_like(self, request, pk=None):
        """Поставить/убрать лайк посту"""
        post = self.get_object()
        user = request.user
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
            return Response({'status': 'unliked'})
        else:
            post.likes.add(user)
            return Response({'status': 'liked'})

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def toggle_like(self, request, pk=None):
        """Поставить/убрать лайк комментарию"""
        comment = self.get_object()
        user = request.user
        if comment.likes.filter(id=user.id).exists():
            comment.likes.remove(user)
            return Response({'status': 'unliked'})
        else:
            comment.likes.add(user)
            return Response({'status': 'liked'})

    @action(detail=False, methods=['get'])
    def most_liked(self, request):
        """Получить комментарии, отсортированные по количеству лайков"""
        comments = Comment.objects.annotate(likes_count=Count('likes')).order_by('-likes_count')[:5]
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)