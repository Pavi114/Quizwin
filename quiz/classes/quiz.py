from quiz.models import Quiz as QuizModel, Round
from quiz.classes.round import get_round

class Quiz:
    def __init__(self, quiz):
        self.quiz = quiz
        self.rounds = [get_round(r) for r in Round.objects.filter(quiz=self.quiz)]

    def info():
        return {
            'name': self.quiz.name,
            'host': self.quiz.host.username,
        }

    @staticmethod
    def create(quiz_info):
        return QuizModel.objects.create(**quiz_info)

    @staticmethod
    def edit(quiz_id, quiz_info):
        return QuizModel.objects.filter(pk=quiz_id).update(**quiz_info)

    def delete(self):
        [r.delete() for r in self.rounds]