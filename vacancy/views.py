from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.expressions import F
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.views.generic.base import View
from .models import Vacancy, Employer
from .forms import CommentForm, VacancyCreateForm


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancy/list.html'
    paginate_by = 10
    context_object_name = 'vacancies'
    ordering = ['-date_created']



class VacancyDetailView(View):
    def increment_view(self, event):
        """ view incerementer """

        event.views = F('views') + 1
        event.save()
        event.refresh_from_db()

    def post(self, request, pk):
        vacancy = get_object_or_404(Vacancy, id = pk)
        comments = vacancy.v_comments.filter(active = True)
        new_comment = None
        comment_form = CommentForm(data = request.POST, files = request.FILES)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.vacancy = vacancy
            new_comment.author = request.user
            new_comment.save()
            comment_form = CommentForm()
        else:
            comment_form = CommentForm() 

        context = {'post':vacancy,
                'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form}

        return render(request, 'vacancy/detail.html', context)

    def get(self, request, pk):
        vacancy = get_object_or_404(Vacancy, id = pk)
        comments = vacancy.v_comments.filter(active = True)
        new_comment = None 
        comment_form = CommentForm()

        context = {'vacancy':vacancy,
                'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form}
        self.increment_view(vacancy)
        return render(request, 'vacancy/detail.html', context)




class VacancyCreateView(LoginRequiredMixin,CreateView):
    form_class = VacancyCreateForm
    template_name = 'vacancy/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class CreateEmployerView(LoginRequiredMixin,View):
    def post(self, request):
        name = request.POST.get('name')
        founded_at = request.POST.get('founded_at')
        if founded_at:
            emp = Employer.objects.create(name = name, founded_at = founded_at)
        else:
            emp = Employer.objects.create(name = name)
        emp.save()
        context = {'code':200, 'emp_id': emp.id}
        return JsonResponse(context)


class VacancyUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=Vacancy
    fields = ['title', 'employer', 'content', 'contact', 'min_salary', 'dead_line', 'freelance']
    template_name = 'vacancy/create.html'

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
    template_name = 'vacancy/delete.html'
    success_url = '/vacancies'

    def test_func(self):
        vacancy = self.get_object()
        return self.request.user == vacancy.author
