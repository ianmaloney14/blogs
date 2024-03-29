from django.urls import path
from .views import HomeView, ArticleDetailView, TemplateView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, PortfolioView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', PortfolioView.as_view(), name="portfolio"),
    path('blog', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-details"),
    path('about/', TemplateView.as_view(template_name="about.html"), name="about"),
    path('terms/', TemplateView.as_view(template_name="terms.html"), name="terms"),
    path('privacy/', TemplateView.as_view(template_name="privacy.html"), name="privacy"),
    path('add-post/', AddPostView.as_view(), name="add-post"),
    path('add-category/', AddCategoryView.as_view(), name="add-category"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update-post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete-post"),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    # path('all-articles', AllArticles.as_view(), name="all-articles"),
]

urlpatterns += staticfiles_urlpatterns()