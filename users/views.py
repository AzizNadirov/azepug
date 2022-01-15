import imp
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.core.paginator import Paginator

from blog.models import Post

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username')
            messages.success(request, f'Qeydiyyat uğurla tamamlandı. Zəhmət olmasa yenidən daxil olun {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request,'users/register.html',{'form': form} )

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES,  instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Dəyişiklik uğurla tamamlandı.')
            return redirect('profile')
        else:
            print('Err:',u_form.errors, p_form.errors)

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user)

    context = {'u_form':u_form,'p_form':p_form}
    return render(request, 'users/edit_profile.html', context)

@login_required
def profile(request):
    user = request.user
    user_post_queryset = Post.objects.filter(author__id=user.id).order_by('-date_created')
    paginator = Paginator(user_post_queryset, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {"user_arts": user_post_queryset,
               'is_paginated': True, 'page_obj': page_obj}
    return render(request, 'users/profile.html', context)

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