from django.urls import path
from django.contrib.auth.views import LoginView

from quiz.views import actions, profile

urlpatterns = [
    path('', actions.join, name='index'),
    path('create', actions.create, name='create'),
    path('accounts/profile/', profile.ProfileView.as_view(), name='profile')
]