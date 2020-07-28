from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView ,DetailView, DeleteView, UpdateView
from .models import Vacancy

class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancy/vacancy_list.html'
    paginate_by = 5
    context_object_name = 'vacancies'
    ordering = ['-date_created']

class VacancyDetailView(DetailView):
    template_name = 'vacancy/about_vacancy.html'
    model = Vacancy
    fields = ['title', 'content', 'dead_line', 'freelance', "date_created"]
    ordering = ["-date_created"]



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
