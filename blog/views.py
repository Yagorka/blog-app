from django.shortcuts import render

# Create your views here.
from .models import Post
from django.views.generic import ListView, DetailView  # new


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView): # new
    model = Post
    template_name = 'post_detail.html'