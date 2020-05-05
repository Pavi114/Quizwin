from collections import defaultdict

from django.forms import model_to_dict

from quiz.models import Round, Question

class BaseRound:
    def __init__(self, round):
        self.round = round

    def info(self):
        return model_to_dict(self.round)

    @staticmethod
    def create(round_info):
        return Round.objects.create(**round_info)

class SequentialRound(BaseRound):
    def __init__(self, round):
        assert round.type == 'Sequential'
        super().__init__(round)

    def info(self):
        info = super().info()
        info['questions'] = [model_to_dict(q) for q in Question.objects.filter(round=self.round)]
        return info

    # TODO depending on how sockets work
    def next_question(self):
        pass
    
class BoardRound(BaseRound):
    def __init__(self, round):
        assert round.type == 'Board'
        super().__init__(round)

    def info(self):
        info = super().info()
        
        questions = defaultdict(list)
        for q in Question.objects.filter(round=self.round).order_by('points'):
            questions[q.category].append(model_to_dict(q))
        info['questions'] = questions

        return info

rounds = {
    'Sequential': SequentialRound,
    'Board': BoardRound
}

def get_round(round):
    return rounds[round.type](round)

def create_round(round_info):
    return rounds[round_info.type].create(round_info)