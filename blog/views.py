from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,CreateView, DeleteView, UpdateView
from django.views.generic.base import View
from django.db.models.expressions import F

from.models import Post
from .forms import CommentForm, CreatePostForm



class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    paginate_by = 4
    context_object_name = 'posts'
    ordering = ['-date_created']




class PostDetailView(View):
    def increment_view(self, post):
        """ view incerementer """

        post.views = F('views') + 1
        post.save()
        post.refresh_from_db()

    def post(self, request, pk):
        post = get_object_or_404(Post, id = pk)
        comments = post.b_comments.filter(active = True)
        new_comment = None
        comment_form = CommentForm(data = request.POST, files=request.FILES)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            comment_form = CommentForm()
        else:
            comment_form = CommentForm()

        context = {'post':post,'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form}
        return render(request, 'blog/detail.html', context)
    

    def get(self, request, pk):
        post = get_object_or_404(Post, id = pk)
        comments = post.b_comments.filter(active = True)
        new_comment = None
        comment_form = CommentForm()
        context = {'post':post,'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form}
        self.increment_view(post)
        return render(request, 'blog/detail.html', context)
    
class PostLikeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        postid = int(request.POST.get('postid'))
        value = request.POST.get('value')
        if value == "like":
            request.user.liked_posts.add(postid)
        elif value == 'unlike':
            request.user.liked_posts.remove(postid)
        return HttpResponse('<h1>Success</h1>', status = 200)

class PostSaveView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        postid = int(request.POST.get('postid'))
        value = request.POST.get('value')
        if value == "save":
            request.user.treasure.blogs.add(postid)
        elif value == 'unsave':
            request.user.treasure.blogs.remove(postid)

        return HttpResponse('<h1>Success</h1>', status = 200)
        
class PostCreateView(LoginRequiredMixin,CreateView):
    form_class = CreatePostForm
    template_name = 'blog/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'tags', 'content']
    template_name = 'blog/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = '/posts'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author