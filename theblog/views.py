from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# def home(request):
#     return render(request, 'theblog/index.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'theblog/index.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'theblog/article_details.html'
