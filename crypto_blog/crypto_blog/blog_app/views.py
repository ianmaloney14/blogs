from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id']
    ordering = ['-created_at']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AllArticles(ListView):
    model = Post
    template_name = 'all_articles.html'
    ordering = ['-created_at']

class AddPostView(CreateView):
    model = Post
    template_name = 'create_article.html'
    fields = '__all__'