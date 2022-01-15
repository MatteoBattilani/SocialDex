from django.shortcuts import render
from django.views.generic import ListView
from posts.models import Post
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixin import StaffMixin

from accounts.forms import UserUpdateForm, ProfileUpdateForm

from django.contrib.auth.decorators import login_required

# This is the library for the ip adresses
from ipware import get_client_ip

# Create your views here.


"""
   This class is the homepage view. It returns a list conteining all the posts.
"""
class PostList(ListView):
    model = Post
    template_name = 'core/homepage.html'
    context_object_name = 'posts'
    ordering = ['-datetime']



"""
Vista che torna un utente grazie alla chiamata "user/nomeutente". E' come la ricerca utente per chiave primaria,
ma in questo caso la ricerca avviene tramite nome utente.
"""
# Using this decorator, to access the page the user have to log in
@login_required
def user_profile_view(request, username):
    # if you are updating your account
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            #messages.success(request, f'Your account has been updated!')
            return redirect("/")
    # if you want to view your account page
    else:
        user= get_object_or_404(User, username=username)
        user_posts= Post.objects.filter(user=user).order_by("-pk")
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context= {'user':user, "user_posts":user_posts, 'u_form': u_form,
            'p_form': p_form}
        return render(request, 'accounts/user_profile.html', context)

"""
    This function returns a list of all the users. Only staff users can access this function.
    If a base user try to access the function he will get "403 Forbidden" error.
"""
# StaffMixin is used in order to permit access the function for staff users only
class UserList(StaffMixin, ListView):
    model= User
    template_name= "core/users.html"




"""
   This function is used to search a word from "base.html"
"""

def cerca(request):
    if "q" in request.GET:
        querystring= request.GET.get("q")
        if len(querystring) == 0:
            return redirect(("/cerca/"))
       # icontains checks that the value associated to the querystring is conteined in title, content and username
        posts_titles= Post.objects.filter(title__icontains=querystring)
        posts_content= Post.objects.filter(content__icontains=querystring)
        users= User.objects.filter(username__icontains=querystring)
        context= {"posts_titles":posts_titles, "posts_content":posts_content, "users":users}
        return render(request, "core/search.html", context)
    else:
        return render(request, "core/search.html")
























