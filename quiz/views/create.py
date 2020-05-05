from django.views import View
from django.shortcuts import render

from quiz.mixins.requires_login import LoginRequiredMixin

class QuizView(LoginRequiredMixin, View):

    def get(self, request, quiz_id):
        '''
        Render the form to create / edit a quiz
        Attributes:
            PARAMS:
                - quiz_id
        '''
        context = {
            'title': 'Quizwin'
        }
        return render(request, 'quiz/index.html', context)

    def put(self, request):
        '''
        Create a quiz
        Attributes:
            none.
        '''
        return {}

    def post(self, request, quiz_id):
        '''
        Edit the attributes of the quiz model
        Attributes:
            PARAMS:
                - quiz_id
            POST:
                - quiz_info
        '''
        return {}

    def delete(self, request, quiz_id):
        '''
        Delete a quiz
        Attributes:
            PARAMS:
                - quiz_id
        '''
        return {}

class RoundView(LoginRequiredMixin, View):

    def get(self, request, quiz_id, round_id):
        '''
        Render the form to create / edit a round
        Attributes:
            PARAMS:
                - quiz_id
                - round_id
        '''

    def put(self, request, quiz_id):
        '''
        Create a round
        Attributes:
            PARAMS:
                - quiz_id
        '''
        return {}

    def post(self, request, quiz_id, round_id):
        '''
        Edit a round
        Attributes:
            PARAMS:
                - quiz_id
                - round_id
            POST:
                - round_info 
        '''
        return {}

    def delete(self, request, quiz_id, round_id):
        '''
        Delete a round
        Attributes:
            PARAMS:
                - quiz_id
                - round_id
        '''
        return {}    

class QuestionView(LoginRequiredMixin, View):

    def get(self, request, quiz_id, round_id, question_id):
        '''
        Render the form to create / edit a question
        Attributes:
            PARAMS:
                - quiz_id
                - round_id
                - question_id
        '''

    def put(self, request, quiz_id, round_id):
        '''
        Create a question
        Attributes:
            PARAMS:
                - quiz_id
                - round_id
        '''
        return {}

    def post(self, request, quiz_id, round_id, question_id):
        '''
        Edit a question
        Attributes:
            PARAMS:
                - quiz_id
                - round_id
                - question_id
            POST:
                - question_info
        '''
        return {}

    def delete(self, request, quiz_id, round_id, question_id):
        '''
        Delete a question
        Attributes:
            PARAMS:
                - quiz_id
                - round_id
                - question_id
        '''
        return {}
