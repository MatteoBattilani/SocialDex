from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name= 'registration'),
    path('<int:pk>/profile/', views.profile, name='profile'),
]