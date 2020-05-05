from django.urls import path
from django.contrib.auth.views import LoginView

from quiz.views import create, join, profile

urlpatterns = [
    path('', join.JoinView.as_view(), name="join"),

    path('accounts/profile/', profile.ProfileView.as_view(), name='profile'),

    # Creating quizzes
    path('create/quiz/', create.QuizView.as_view(), name="create-quiz"),
    path('create/quiz-<int:quiz_id>/', create.QuizView.as_view(), name="edit-quiz"),
    path('create/quiz-<int:quiz_id>/round/', create.RoundView.as_view(), name="create-round"),
    path('create/quiz-<int:quiz_id>/round-<int:round_id>/', create.RoundView.as_view(), name="edit-round"),
    path('create/quiz-<int:quiz_id>/round-<int:round_id>/question/', create.RoundView.as_view(), name="create-question"),
    path('create/quiz-<int:quiz_id>/round-<int:round_id>/question-<int:question_id>/', create.RoundView.as_view(), name="edit-question"),
]