from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 2

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'