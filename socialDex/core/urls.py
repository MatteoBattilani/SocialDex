from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name= 'homepage'),
    path('user/<str:username>/', views.user_profile_view, name='user_profile'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('search/', views.cerca, name='search_function'),
]