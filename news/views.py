from django.db.models.expressions import F
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,CreateView, DeleteView, UpdateView
from django.views.generic.base import View

from.models import News
from .forms import CommentForm, CreateNewsForm



class NewsListView(ListView):
    model = News
    template_name = 'news/list.html'
    paginate_by = 4
    context_object_name = 'news'
    ordering = ['-date_created']


class NewsDetailView(View):
    def increment_view(self, event):
        """ view incerementer """

        event.views = F('views') + 1
        event.save()
        event.refresh_from_db()

    def post(self, request, pk):
        news = get_object_or_404(News, id = pk)
        comments = news.n_comments.filter(active = True)
        new_comment = None
        comment_form = CommentForm(data = request.POST, files=request.FILES)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.news = news
            new_comment.author = request.user
            new_comment.save()
        scomment_form = CommentForm()

        context = {'post':news,'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form}
        return render(request, 'news/detail.html', context)
    

    def get(self, request, pk):
        news = get_object_or_404(News, id = pk)
        comments = news.n_comments.filter(active = True)
        new_comment = None
        comment_form = CommentForm()
        context = {'news':news,'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form}
        self.increment_view(news)
        return render(request, 'news/detail.html', context)


class NewsCreateView(LoginRequiredMixin,CreateView):
    form_class = CreateNewsForm
    template_name = 'news/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewsUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = News
    fields = ['title', 'content', 'tags']
    template_name = 'news/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        return self.request.user == news.author


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = News
    template_name = 'news/delete.html'
    success_url = '/news'

    def test_func(self):
        news = self.get_object()
        return self.request.user == news.author