from django.views import View
from django.shortcuts import render

from quiz.mixins.requires_login import LoginRequiredMixin


class CreateQuestionView(LoginRequiredMixin, View):

    def get(self, request, quiz_id, round_id):
        '''
        Render the form to create a question
        Attributes:
            None
        '''
        context = {}
        return render(request, 'quiz/create/question.html', context)
    
    def post(self, request, quiz_id, round_id):
        '''
        Create a question
        Attributes:
            none.
        '''
        return {}


class EditQuestionView(LoginRequiredMixin, View):

    def get(self, request, quiz_id, round_id, question_id):
        '''
        Render the form to edit a question
        Attributes:
            None
        '''
        context = {}
        return render(request, 'quiz/create/question.html', context)

    def post(self, request, quiz_id, round_id, question_id):
        '''
        Edit the attributes of the question model
        Attributes:
            PARAMS:
                - quiz_id, round_id, question_id
            POST:
                - question_info
        ''' 
        return {}


class DeleteQuestionView(LoginRequiredMixin, View):

    def post(self, request, quiz_id, round_id, question_id):
        '''
        Delete a question
        Attributes:
            PARAMS:
                - quiz_id, round_id, question_id
        '''
        return {}   