from django.views import View
from django.shortcuts import render

from quiz.mixins.requires_login import LoginRequiredMixin

class JoinView(LoginRequiredMixin, View):

    def get(self, request):
        '''
        Render form for joining a quiz
        '''
        context = {
            'title': 'Quizwin'
        }
        return render(request, 'quiz/index.html', context)

    def post(self, request):
        '''
        Join a quiz
        Attributes:
            POST:
                - quiz_id
                - quiz_secret
        '''
        return {}