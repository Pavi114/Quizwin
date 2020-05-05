from django.urls import path
from django.contrib.auth.views import LoginView

from quiz.views import create, join, profile

urlpatterns = [
    path('', join.JoinView.as_view(), name="join"),
    path('create', create.QuizView.as_view(), name="create"),
    path('accounts/profile/', profile.ProfileView.as_view(), name='profile')
]