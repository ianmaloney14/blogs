from django.urls import path
from .views import HomeView, ArticleDetailView, TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-details"),
    path('about/', TemplateView.as_view(template_name="about.html"), name="about"),
    # path('all-articles', AllArticles.as_view(), name="all-articles"),
    # path('create-article', AddPostView.as_view(), name="create-article"),
]

urlpatterns += staticfiles_urlpatterns()