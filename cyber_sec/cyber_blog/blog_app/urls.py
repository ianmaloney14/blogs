from django.urls import path
from .views import HomeView, ArticleDetailView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-details"),
]

urlpatterns += staticfiles_urlpatterns()