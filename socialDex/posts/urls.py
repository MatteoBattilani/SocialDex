from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts, name= 'posts'),
    path('new-post/', views.CreatePost.as_view(), name='new_post'),
    path('post_detail/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/update', views.PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete', views.PostDelete.as_view(), name='post_delete'),
]