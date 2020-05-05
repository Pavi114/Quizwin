class Quiz:
    def __init__(self, quiz):
        self.quiz = quiz

    def info():
        return {
            'name': self.quiz.name,
            'host': self.quiz.host.username,
        }

    @staticmethod
    def create(quiz_info):
        return Quiz.objects.create(**quiz_info)