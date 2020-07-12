from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.generic import ListView,CreateView,DetailView,DeleteView

from.models import Post

#------------------- show post -------------


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 4
    context_object_name = 'posts'
    ordering = ['-date_created']

class PostDetailView(DetailView):
    template_name = 'blog/about_post.html'
    model = Post
    fields = "__all__"

class PostCreateView(CreateView):
    model=Post
    fields = ['title', 'category', 'content', 'slug']