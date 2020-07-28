from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

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

def profile(request):
    return render(request, 'users/profile.html')