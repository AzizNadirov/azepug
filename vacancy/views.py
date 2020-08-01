from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Vacancy
from blog.forms import GuestCommentForm, UserCommentForm


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancy/vacancy_list.html'
    paginate_by = 5
    context_object_name = 'vacancies'
    ordering = ['-date_created']

def vacancy_detail(request, pk):
    # check user and select kind of comment form
    if request.user.is_authenticated:
        CommentForm = UserCommentForm
    else:
        CommentForm = GuestCommentForm
    vacancy = get_object_or_404(Vacancy, id = pk)
    comments = vacancy.comments.filter(active = True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.vacancy = vacancy
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'vacancy/about_vacancy.html', {'vacancy':vacancy,
     'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form})



class VacancyCreateView(LoginRequiredMixin,CreateView):
    model=Vacancy
    fields = ['title', 'content', 'dead_line', 'freelance']
    template_name = 'vacancy/CRUD_vacancy/create_vacancy.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class VacancyUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=Vacancy
    fields = ['title', 'content', 'dead_line', 'freelance']
    template_name = 'vacancy/CRUD_vacancy/create_vacancy.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        vacancy = self.get_object()
        if self.request.user == vacancy.author:
            return True
        else: return False

class VacancyDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Vacancy
    template_name = 'vacancy/CRUD_vacancy/delete_vacancy.html'
    success_url = '/vacancies'

    def test_func(self):
        vacancy = self.get_object()
        if self.request.user == vacancy.author:
            return True
        else: return False
