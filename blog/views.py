from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,CreateView, DeleteView, UpdateView
from django.views.generic.base import View

from.models import Post
from .forms import CommentForm, CreatePostForm



class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 4
    context_object_name = 'posts'
    ordering = ['-date_created']




class PostDetailView(View):
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
        return render(request, 'blog/about_post.html', context)
    

    def get(self, request, pk):
        post = get_object_or_404(Post, id = pk)
        comments = post.b_comments.filter(active = True)
        new_comment = None
        comment_form = CommentForm()
        context = {'post':post,'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form}
        return render(request, 'blog/about_post.html', context)


class PostCreateView(LoginRequiredMixin,CreateView):
    # model = Post
    # fields = ['title', 'category', 'content']
    form_class = CreatePostForm
    template_name = 'blog/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'tags', 'content']
    template_name = 'blog/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = '/blogs'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author