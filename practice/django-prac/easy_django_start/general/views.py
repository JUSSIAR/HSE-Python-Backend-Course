from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


from .models import Article
from .models import Comment

from .serializers import ArticleSerializer
from .serializers import CommentSerializer


class ArticleAPIViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(methods=['GET'], detail=False)
    def info(self, request):
        return Response({
            'info': 'API Info is here'
        })


class CommentAPIViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


