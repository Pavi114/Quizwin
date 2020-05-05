from django.urls import path
from django.contrib.auth.views import LoginView

from quiz.views import join, profile, quiz, round, question

urlpatterns = [
    path('', join.JoinView.as_view(), name="join"),

    path('accounts/profile/', profile.ProfileView.as_view(), name='profile'),

    # Creating quizzes
    path('create/quiz/', quiz.CreateQuizView.as_view(), name="create-quiz"),
    path('create/quiz-<int:quiz_id>/round/', round.CreateRoundView.as_view(), name="create-round"),
    path('create/quiz-<int:quiz_id>/round-<int:round_id>/question/', question.CreateQuestionView.as_view(), name="create-question"),

    # Editing quizzes
    path('edit/quiz-<int:quiz_id>/', quiz.EditQuizView.as_view(), name="edit-quiz"),
    path('edit/quiz-<int:quiz_id>/round-<int:round_id>/', round.EditRoundView.as_view(), name="edit-round"),
    path('edit/quiz-<int:quiz_id>/round-<int:round_id>/question-<int:question_id>/', question.EditQuestionView.as_view(), name="edit-question"),

    # Deleting quizzes
    path('delete/quiz-<int:quiz_id>/', quiz.DeleteQuizView.as_view(), name="delete-quiz"),
    path('delete/quiz-<int:quiz_id>/round-<int:round_id>/', round.DeleteRoundView.as_view(), name="delete-round"),
    path('delete/quiz-<int:quiz_id>/round-<int:round_id>/question-<int:question_id>/', question.DeleteQuestionView.as_view(), name="delete-question"),
]