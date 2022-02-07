from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.paginator import Paginator
from django.views.generic import View

from .forms import UserRegistrationForm, ProfileUpdateForm

from blog.models import Post
from events.models import Event
from forum.models import Answer
from forum.models import Question
from news.models import News
from vacancy.models import Vacancy

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('user_name')
            messages.success(request, f'Qeydiyyat uğurla tamamlandı. Zəhmət olmasa yenidən daxil olun {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request,'users/register.html',{'form': form} )

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES,  instance = request.user)

        if form.is_valid():
            form.save()
            messages.success(request, f'Dəyişiklik uğurla tamamlandı.')
            return redirect('profile')

    else:
        form = ProfileUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user)

    context = {'form':form}
    return render(request, 'users/edit_profile.html', context)

# @login_required
# def profile(request):
#     user = request.user
#     user_post_queryset = Post.objects.filter(author__id=user.id).order_by('-date_created')
#     paginator = Paginator(user_post_queryset, 2)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     context = {"user_arts": user_post_queryset,
#                'is_paginated': True, 'page_obj': page_obj}
#     return render(request, 'users/profile.html', context)

class Profile(LoginRequiredMixin, View):
    RECENT_NUM = 3
    def get(self, request):
        user = request.user
        post_queryset = Post.objects.filter(author__id=user.id).order_by('-date_created')[:self.RECENT_NUM]
        news_queryset = News.objects.filter(author__id=user.id).order_by('-date_created')[:self.RECENT_NUM]
        vacancy_queryset = Vacancy.objects.filter(author__id=user.id).order_by('-date_created')[:self.RECENT_NUM]
        event_queryset = Event.objects.filter(author__id=user.id).order_by('-date_created')[:self.RECENT_NUM]
        answer_queryset = Answer.objects.filter(author__id=user.id).order_by('-date_created')[:self.RECENT_NUM]
        question_queryset = Question.objects.filter(author__id=user.id).order_by('-date_created')[:self.RECENT_NUM]

        recents_queryset = {'news': news_queryset, 'post':post_queryset, 'vacancy':vacancy_queryset, 'event':event_queryset,
                                'answer':answer_queryset, 'question':question_queryset}
        r = list(recents_queryset.values())

        context = {'recents':recents_queryset}
        return render(request, 'users/profile.html', context)
    
    def post(self, request):
        return HttpResponse("<h1>Post request to Profile detected</h1>")

def user(request, username):
    # NUM_TOP_ARTS = 10
    user = get_object_or_404(settings.AUTH_USER_MODEL, user_name = username)
    user_articles_queryset = Post.published.filter( author__id = user.id).order_by('-date_created')

    paginator = Paginator(user_articles_queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.user.user_name == username:
        owner = True
    else:
        owner = False
    context = {'u': user, "articles":user_articles_queryset,
               'is_paginated':True, 'page_obj':page_obj}
    return render(request, 'users/user.html',context)