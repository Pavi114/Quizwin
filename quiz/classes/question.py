from django.forms import model_to_dict
from django.db.models import F

from quiz.models import Question, QuestionSlide, NormalAnswer, Choice, ChoiceAnswer, OrderAnswer, QuestionScores, Score
from quiz.classes.slide import get_slide, create_slide
from quiz.constants import QuestionType

class BaseQuestion:
    def __init__(self, question):
        self.question = question
        
        self.slides = [
            get_slide(qs.slide) for qs in QuestionSlide.objects.filter(question=self.question)
        ]
    
    def host_info(self):
        info = model_to_dict(self.question)
        return {
            **info,
            'slides': [slide.info() for slide in self.slides],
            'answer': self.answer(),
        }
    
    def player_info(self):
        return model_to_dict(self.question)

    def answer(self):
        pass

    def award_points(self, user, points):
        QuestionScores.objects.create(user=user, question=self.question, score=points)

        quiz_score = Score.objects.get_or_create(quiz=self.question.round.quiz, user=user)
        quiz_score.score += F('score') + points
        quiz_score.save()
    
    @staticmethod
    def create(question_info):
        question = Question.objects.create(**question_info.question)

        slides = [create_slide(slide) for slide in question_info.slides]
        for i, slide in enumerate(slides):
            QuestionSlide.objects.create(
                question=question,
                slide=slide,
                slide_number=i
            )

        return question

    def edit(self, question_info):
        self.question.__dict__.update(question_info.question)
        self.question.save()

        QuestionSlide.objects.filter(question=self.question).delete()
        for slide in self.slides:
            slide.delete()

        slides = [create_slide(slide) for slide in question_info.slides]
        for i, slide in enumerate(slides):
            QuestionSlide.objects.create(
                question=self.question,
                slide=slide,
                slide_number=i
            )

    def delete(self):
        for slide in self.slides:
            slide.delete()

        self.question.delete()

class NormalQuestion(BaseQuestion):
    def __init__(self, question):
        assert question.type == QuestionType.NORMAL

        super().__init__(question)

        self.answer = NormalAnswer.objects.get(question=self.question)
        self.answer_slide = get_slide(self.answer.slide)

    def answer(self):
        return self.answer_slide.info()

    def award_points(self, user):
        question_score = self.question.points * self.question.multiplier
        super().award_points(user, question_score)

    @staticmethod
    def create(question_info):
        question = BaseQuestion.create(question_info)

        answer_slide = create_slide(question_info.answer)
        answer = NormalAnswer.objects.create(
            question=question,
            slide=answer_slide
        )

        return question

    def edit(self, question_info):
        super().edit(question_info)

        self.answer_slide.delete()

        answer_slide = create_slide(question_info.answer)
        NormalAnswer.objects.create(
            question=self.question,
            slide=answer_slide
        )

    def delete(self):
        self.answer_slide.delete()
        super().delete()

class ChoiceQuestion(BaseQuestion):
    def __init__(self, question):
        assert question.type == QuestionType.MCQ

        super().__init__(question)

        self.choices = Choice.objects.filter(question=self.question)
        self.choice_slides = [get_slide(choice.slide) for choice in self.choices]

        self.answer = ChoiceAnswer.objects.get(question=self.question).choice.choice_number

    def host_info(self):
        info = super().host_info()
        info['choices'] = [slide.info() for slide in self.choice_slides]
        return info

    def player_info(self):
        info = super().player_info()
        info['choices'] = len(self.choice_slides)
        return info

    def answer(self):
        return self.answer

    def award_points(self, user, answer):
        question_points = self.question.points * self.question.multiplier
        
        num_answered = QuestionScores.objects.filter(question=question).count()

        if answer == self.answer:
            degradation = self.question.degradation ** num_answered
        else:
            degradation = - ((1 - self.question.degradation) ** num_answered)

        question_points = question_points * degradation
        super().award_points(user, question_points)

    @staticmethod
    def create(question_info):
        question = BaseQuestion.create(question_info)

        choice_slides = [create_slide(slide) for slide in question_info.choices]
        for i, slide in enumerate(choice_slides):
            choice = Choice.objects.create(
                question=question,
                slide=slide,
                choice_number=i
            )
            if i == question_info.answer:
                ChoiceAnswer.objects.create(
                    question=question,
                    choice=choice
                )

        return question

    def edit(self, question_info):
        super().edit(question_info)

        for slide in self.choice_slides:
            slide.delete()

        choice_slides = [create_slide(slide) for slide in question_info.choices]
        for i, slide in enumerate(choice_slides):
            choice = Choice.objects.create(
                question=question,
                slide=slide,
                choice_number=i
            )
            if i == question_info.answer:
                ChoiceAnswer.objects.create(
                    question=question,
                    choice=choice
                )

    def delete(self):
        for slide in self.choice_slides:
            slide.delete()

        super().delete()

class OrderQuestion(BaseQuestion):
    def __init__(self, question):
        assert question.type == QuestionType.ORDERING

        super.__init__(question)

        self.choices = Choice.objects.filter(question=self.question)
        self.choice_slides = [get_slide(choice.slide) for choice in self.choices]

        self.answer = OrderAnswer.objects.get(question=self.question).order

    def host_info(self):
        info = super().host_info()
        info['choices'] = [slide.info() for slide in self.choice_slides]
        return info

    def player_info(self):
        info = super().player_info()
        info['choices'] = len(self.choice_slides)
        return info
    
    def answer(self):
        return {
            order: [int(x) for x in list(self.answer)]
        }
    
    def award_points(self, user, answer):
        question_points = self.question.points * self.question.multiplier
        
        num_answered = QuestionScores.objects.filter(question=question).count()

        if answer == self.answer:
            degradation = self.question.degradation ** num_answered
        else:
            degradation = - ((1 - self.question.degradation) ** num_answered)

        question_points = question_points * degradation
        super().award_points(user, question_points)

    @staticmethod
    def create(question_info):
        question = BaseQuestion.create(question_info)

        choice_slides = [create_slide(slide) for slide in question_info.choices]
        for i, slide in enumerate(choice_slides):
            choice = Choice.objects.create(
                question=question,
                slide=slide,
                choice_number=i
            )
        
        OrderAnswer.objects.create(
            question=question,
            order=question_info.order
        )

        return question

    def edit(self, question_info):
        super().edit(question_info)

        OrderAnswer.objects.get(question=self.question).delete()
        for slide in self.choice_slides:
            slide.delete()

        choice_slides = [create_slide(slide) for slide in question_info.choices]
        for i, slide in enumerate(choice_slides):
            choice = Choice.objects.create(
                question=question,
                slide=slide,
                choice_number=i
            )
        
        OrderAnswer.objects.create(
            question=question,
            order=question_info.order
        )

    def delete(self):
        for slide in self.choice_slides:
            slide.delete()

        super().delete()

questions = {
    QuestionType.NORMAL: NormalQuestion,
    QuestionType.MCQ: ChoiceQuestion,
    QuestionType.ORDERING: OrderQuestion,
}

def get_question(question):
    return questions[question.type](question)

def create_question(question_info):
    return questions[question_info.type].create(question_info)

def edit_question(question, question_info):
    questions[question.type](question).edit(question_info)

def delete_question(question):
    questions[question.type](question).delete()