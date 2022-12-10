from django.urls import path
from .views import HomeView, ArticleDetailView, AllArticles, AddPostView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('all-articles', AllArticles.as_view(), name="all-articles"),
    path('create-article', AddPostView.as_view(), name="create-article"),
]

urlpatterns += staticfiles_urlpatterns()