from django.shortcuts import render
from django.http import  JsonResponse
from .models import Post
from .forms import PostForm

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.utils import timezone
from datetime import timedelta

# Create your views here.


def posts24(request):
    """
          posts function returns a JSON list of all posts created in the last hour.
    """
    response = []
    last_hour = timezone.now() - timedelta(hours=1)
    posts = Post.objects.filter(datetime__gte=last_hour)
    for post in posts:
        response.append(
            {
                'datetime': post.datetime,
                'content': post.content,
                'author': f"{post.user.first_name} {post.user.last_name}",
                'hash': post.hash,
                'txId': post.txId
            }
        )
    return JsonResponse(response, safe=False, )



def posts(request):
    """
          posts function returns a JSON list of all posts created in the last hour.
    """
    response = []
    posts = Post.objects.filter().order_by('-datetime')
    for post in posts:
        response.append(
            {
                'datetime': post.datetime,
                'title': post.title,
                'content': post.content,
                'author': f"{post.user.first_name} {post.user.last_name}",
                'hash': post.hash,
                'txId': post.txId
            }
        )
    return JsonResponse(response, safe=False)



"""
     The function allows to create a new post. Only registred user can write a post, so login is required.
"""
# LoginRequiredMixin is used to block the access to the new post creation page if the user is not logged in.
class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/new_post.html'
    success_url = '/'

    # Overriding the methot in order to set as author the current author.
    def form_valid(self, form):
        form.instance.user = self.request.user
        post = form.save(commit=False)
        post.writeOnChain()  # in order to write the post in the blockchain automatically
        return super().form_valid(form)





"""
     The function allows to access the datail of a post. 
"""

class PostDetail(DetailView):
    model = Post
    template_name = "posts/post_detail.html"





"""
    This function allows, the owner of the post, to edit it.
    Only the owner of the post can do it.
"""

# UserPassesTestMixin is used in order to allow only the author of a post to edit it.
class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ('title', 'content')
    template_name = 'posts/update_post.html'

    # Overriding the method in order to set as author the current author.
    def form_valid(self, form):
        form.instance.user = self.request.user
        post = form.save(commit=False)
        post.writeOnChain()
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

    # This function returns the page of the post edited
    def return_edited_post(self):
        return posts.get_absolute_url()



"""
    This function allows, the owner of a post, to delete it.
    Only the owner of the post can delete it.
"""

# UserPassesTestMixin is used in order to allow only the author of a post to delete it.
class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # succes_url is used to redirect the user to homepage after he's deleted the post
    template_name = 'posts/post_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

