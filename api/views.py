from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer


# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
  
