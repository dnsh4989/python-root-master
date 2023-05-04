from django.urls import path, include

from .views import ArticlesFrontendAPIView, ArticlesBackendAPIView, ArticleByIdAPIView

urlpatterns = [
    path('', include('common.urls')),
    path('articles/frontend/', ArticlesFrontendAPIView.as_view()),
    path('articles/backend/', ArticlesBackendAPIView.as_view()),
    path('articles/details/<str:id>', ArticleByIdAPIView.as_view()),
]