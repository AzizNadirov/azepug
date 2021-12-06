from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
        p_form = ProfileUpdateForm(instance = request.user.profile)
        print(u_form.is_valid() and p_form.is_valid())

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Dəyişiklik uğurla tamamlandı.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

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
    user = get_object_or_404(User, username = username)
    user_articles_queryset = Post.published.filter( author__id = user.id).order_by('-date_created')

    paginator = Paginator(user_articles_queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.user.username == username:
        owner = True
    else:
        owner = False
    context = {'s_user': user, 'is_owner': owner, "articles":user_articles_queryset,
               'is_paginated':True, 'page_obj':page_obj}
    return render(request, 'users/profile.html',context)