from django.urls import path, include

from .views import ArticlesFrontendAPIView, ArticlesBackendAPIView

urlpatterns = [
    path('', include('common.urls')),
    path('articles/frontend/', ArticlesFrontendAPIView.as_view()),
    path('articles/backend/', ArticlesBackendAPIView.as_view()),
]