from django.urls import path
from .views import HomeView, ArticleDetailView, TemplateView, AddPostView, UpdatePostView, DeletePostView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-details"),
    path('about/', TemplateView.as_view(template_name="about.html"), name="about"),
    path('add-post/', AddPostView.as_view(), name="add-post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update-post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete-post"),
    # path('all-articles', AllArticles.as_view(), name="all-articles"),
]

urlpatterns += staticfiles_urlpatterns()