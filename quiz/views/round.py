from django.views import View
from django.shortcuts import render

from quiz.mixins.requires_login import LoginRequiredMixin


class CreateRoundView(LoginRequiredMixin, View):

    def get(self, request, quiz_id):
        '''
        Render the form to create a round
        Attributes:
            None
        '''
        context = {}
        return render(request, 'quiz/create/round.html', context)
    
    def post(self, request, quiz_id):
        '''
        Create a round
        Attributes:
            none.
        '''
        return {}


class EditRoundView(LoginRequiredMixin, View):

    def get(self, request, quiz_id, round_id):
        '''
        Render the form to edit a round
        Attributes:
            None
        '''
        context = {}
        return render(request, 'quiz/create/round.html', context)

    def post(self, request, quiz_id, round_id):
        '''
        Edit the attributes of the round model
        Attributes:
            PARAMS:
                - quiz_id, round_id
            POST:
                - round_info
        ''' 
        return {}


class DeleteRoundView(LoginRequiredMixin, View):

    def post(self, request, quiz_id, round_id):
        '''
        Delete a round
        Attributes:
            PARAMS:
                - quiz_id, round_id
        '''
        return {}   