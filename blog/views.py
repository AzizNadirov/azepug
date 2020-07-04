from django.shortcuts import render, get_object_or_404
from.models import Post

def blog_list(request):
    posts = Post.published.all()
    return render(request, 'blog/blog_list.html', {'posts' : posts})
    
def about_post(request, year, day, month, post):
    post = get_object_or_404(Post,
    publish__year = year,
    publish__month = month,
    publish__day = day)
    return render(request, 'blog/about_post.html', {'post' : post})
