from django.shortcuts import render, get_object_or_404, redirect
# from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,CreateView, DeleteView, UpdateView

from.models import Post
from .forms import GuestCommentForm, UserCommentForm

#------------------- show post -------------


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 4
    context_object_name = 'posts'
    ordering = ['-date_created']



def post_detail(request, pk):
    # check user and select kind of comment form
    if request.user.is_authenticated:
        CommentForm = UserCommentForm
    else:
        CommentForm = GuestCommentForm

    post = get_object_or_404(Post, id = pk)
    comments = post.comments.filter(active = True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/about_post.html', {'post':post,
     'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form})



class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields = ['title', 'category', 'content']
    template_name = 'blog/CRUD_post/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=Post
    fields = ['title', 'category', 'content']
    template_name = 'blog/CRUD_post/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else: return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Post
    template_name = 'blog/CRUD_post/delete_post.html'
    success_url = '/blogs'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else: return False