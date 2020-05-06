from collections import defaultdict

from django.forms import model_to_dict

from quiz.models import Round, Question
from quiz.classes.question import delete_question
from quiz.constants import RoundType

class BaseRound:
    def __init__(self, round):
        self.round = round
        self.questions = Question.objects.filter(round=self.round)

    def info(self):
        return model_to_dict(self.round)

    def base_info(self):
        return model_to_dict(self.round)

    @staticmethod
    def create(round_info):
        return Round.objects.create(**round_info)

    @staticmethod
    def edit(round_id, round_info):
        return Round.objects.filter(pk=round_id).update(**round_info)

    def delete(self):
        [delete_question(q) for q in self.questions]
        self.round.delete()

class SequentialRound(BaseRound):
    def __init__(self, round):
        assert round.type == RoundType.SEQUENTIAL
        super().__init__(round)

    def info(self):
        info = super().info()
        info['questions'] = [model_to_dict(q) for q in self.questions]
        return info

    # TODO depending on how sockets work
    def next_question(self):
        pass
    
class BoardRound(BaseRound):
    def __init__(self, round):
        assert round.type == RoundType.BOARD
        super().__init__(round)

    def info(self):
        info = super().info()
        
        questions = defaultdict(list)
        for q in self.questions.order_by('points'):
            questions[q.category].append(model_to_dict(q))
        info['questions'] = questions

        return info

rounds = {
    RoundType.SEQUENTIAL: SequentialRound,
    RoundType.BOARD: BoardRound
}

def get_round(round):
    print(round.type)
    return rounds[round.type](round)

def create_round(round_info):
    return rounds[round_info.type].create(round_info)

def edit_round(round_id, round_info):
    return rounds[round_info.type].edit(round_id, round_info)

def delete_round(round):
    rounds[round.type](round).delete()