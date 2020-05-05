from django.views.generic import ListView

from quiz.mixins.requires_login import LoginRequiredMixin
from quiz.models import Quiz

class ProfileView(LoginRequiredMixin, ListView):
    # template_name = 'quiz/my.html'
    model = Quiz
    paginate_by = 10
    context_object_name = 'quizzes'

    def get_queryset(self):
        return Quiz.objects.filter(host=self.request.user)