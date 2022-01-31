from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


"""
   This function allows users to sign up the site
"""


def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f'{username}, your account has been created! You are now able to log in!')
            # after registration, user is redirected on login page
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/registration.html', {'form': form})


"""
    This function allows to access / update the profile page
"""

# Using this decorator, to access the page the user have to log in


@login_required
def profile(request, pk):
    # if you are updating your account
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect("/")
    # if you want to view your account page
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/user_profile.html', context)
