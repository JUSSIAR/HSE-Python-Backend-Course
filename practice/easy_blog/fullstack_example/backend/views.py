from rest_framework import viewsets

from .models import Article
from .models import Comment

from .serializers import ArticleSerializer
from .serializers import CommentSerializer


class ArticleAPIViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentAPIViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
