from django.views import View
from django.shortcuts import render

from quiz.mixins.requires_login import LoginRequiredMixin


class CreateQuizView(LoginRequiredMixin, View):

    def get(self, request):
        '''
        Render the form to create a quiz
        Attributes:
            None
        '''
        context = {}
        return render(request, 'quiz/create/quiz.html', context)
    
    def post(self, request):
        '''
        Create a quiz
        Attributes:
            none.
        '''

        return {}


class EditQuizView(LoginRequiredMixin, View):

    def get(self, request, quiz_id):
        '''
        Render the form to edit a quiz
        Attributes:
            None
        '''
        context = {}
        return render(request, 'quiz/create/quiz.html', context)

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


class DeleteQuizView(LoginRequiredMixin, View):

    def post(self, request, quiz_id):
        '''
        Delete a quiz
        Attributes:
            PARAMS:
                - quiz_id
        '''
        return {}   