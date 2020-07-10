from django.shortcuts import render, redirect
from .forms import CustomRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method=="POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("new user created, log in to get started"))
            return redirect('register')
    else:
        register_form = CustomRegisterForm()    
    return render(request, 'register.html', {'register_form': register_form})





@login_required
def profile(request):
    if request.method=="POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, ('Your Account has been Updated'))
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html',context)