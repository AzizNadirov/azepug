from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.generic import ListView

from.models import Post
from .forms.add_post import PostForm

#------------------- show post --------------------------------
def blog_list(request):
    posts = Post.published.all().order_by('-date_created')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog_list.html', {'posts' : posts ,'page': page})
    
def about_post(request, year, day, month, post):
    post = get_object_or_404(Post,
    slug = post,
    date_created__year = year,
    date_created__month = month,
    date_created__day = day)
    return render(request, 'blog/about_post.html', {'post' : post})

#----------------------- form create post ---------------------------

def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'blog/CU_form.html', context)

def update_post(requst, pk):
    post = Post.published.get(id = pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'blog/CU_form.html', context)
class BlogList_v(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 9
    template_name = 'blog/blog_list.html'
