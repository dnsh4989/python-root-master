import math, random, time, string

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_redis import get_redis_connection
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.authentication import JWTAuthentication
from common.serializers import UserSerializer
from .serializer import ArticleSerializer
from core.models import Article, User
from django.core.cache import cache


class ArticlesFrontendAPIView(APIView):
    @method_decorator(cache_page(60 * 60 * 2, key_prefix='articles_frontend'))
    def get(self, _):
        time.sleep(2)
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticlesBackendAPIView(APIView):

    def get(self, request):
        articles = cache.get('articles_backend')
        if not articles:
            time.sleep(2)
            articles = list(Article.objects.all())
            cache.set('articles_backend', articles, timeout=60 * 30)  # 30 min

        s = request.query_params.get('s', '')
        if s:
            articles = list([
                p for p in articles
                if (s.lower() in p.title.lower()) or (s.lower() in p.description.lower())
            ])

        total = len(articles)

        sort = request.query_params.get('sort', None)
        if sort == 'asc':
            articles.sort(key=lambda p: p.price)
        elif sort == 'desc':
            articles.sort(key=lambda p: p.price, reverse=True)

        per_page = 9
        page = int(request.query_params.get('page', 1))
        start = (page - 1) * per_page
        end = page * per_page

        data = ArticleSerializer(articles[start:end], many=True).data
        return Response({
            'data': data,
            'meta': {
                'total': total,
                'page': page,
                'last_page': math.ceil(total / per_page)
            }
        })
