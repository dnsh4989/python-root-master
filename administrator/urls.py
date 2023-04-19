from django.urls import path, include

from .views import SubscriberAPIView, ArticleGenericAPIView

urlpatterns = [
    path('', include('common.urls')),
    path('subscribers/', SubscriberAPIView.as_view()),
    path('articles/', ArticleGenericAPIView.as_view()),
    path('articles/<str:pk>', ArticleGenericAPIView.as_view()),
]