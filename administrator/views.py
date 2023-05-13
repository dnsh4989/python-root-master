from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ArticleSerializer
from common.authentication import JWTAuthentication
from common.serializers import UserSerializer
from core.models import User, Article
from django.core.cache import cache


class SubscriberAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, _):
        subscribers = User.objects.filter(is_subscriber=True)
        serializer = UserSerializer(subscribers, many=True)
        return Response(serializer.data)
    

class ArticleGenericAPIView(
    generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)

        return self.list(request)

    def post(self, request):
        response = self.create(request)
        for key in cache.keys('*'):
            if 'articles_backend' in key:
                cache.delete(key)
        cache.delete('articles_backend')
        return response

    def put(self, request, pk=None):
        response = self.partial_update(request, pk)
        for key in cache.keys('*'):
            if 'articles_backend' in key:
                cache.delete(key)
        cache.delete('articles_backend')
        return response

    def delete(self, request, pk=None):
        response = self.destroy(request, pk)
        for key in cache.keys('*'):
            if 'articles_backend' in key:
                cache.delete(key)
        cache.delete('articles_backend')
        return response
