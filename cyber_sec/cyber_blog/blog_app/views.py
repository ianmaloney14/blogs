from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator

class PortfolioView(ListView):
    model = Post
    template_name = 'portfolio.html'

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 4

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

class CategoryListView(ListView):
    model = Category
    template_name = 'categories_list.html'

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
