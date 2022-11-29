from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id']
    ordering = ['-created_at']

# def home(request):
#     post_list = Post.objects.all()
#     return render(request, 'home.html', {'post_list': post_list})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


