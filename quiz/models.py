from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from quiz.mixins.timestamp import TimestampModel

# Create your models here.
class Quiz(TimestampModel):
    name = models.CharField(max_length=64)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    secret = models.CharField(max_length=32)
    started = models.BooleanField(default=False)
    ended = models.BooleanField(default=False)

class Round(models.Model):
    class RoundType(models.TextChoices):
        SEQUENTIAL = 'S', _('Sequential')
        BOARD = 'B', _('Board')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=RoundType.choices)
    name = models.CharField(max_length=64)

class Text(models.Model):
    text = models.TextField(max_length=512)

class Image(models.Model):
    image = models.URLField()

class Slide(models.Model):
    class SlideType(models.TextChoices):
        TEXT = 'T', _('Text')
        IMAGE = 'I', _('Image')
    type = models.CharField(max_length=1, choices=SlideType.choices)
    fk = models.IntegerField()

class Question(models.Model):
    class QuestionTypes(models.TextChoices):
        NORMAL = 'N', _('Normal')
        MCQ = 'C', _('MCQ')
        ORDERING = 'O', _('Order')
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    question_number = models.IntegerField(null=True)
    category = models.TextField(null=True)
    type = models.TextField(max_length=1, choices=QuestionTypes.choices)
    slides = models.IntegerField(default=1)
    points = models.IntegerField()
    degradation = models.FloatField(default=0)
    multiplier = models.FloatField(default=1)
    done = models.BooleanField(default=False)

class QuestionSlide(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    slide = models.ForeignKey(Slide, on_delete=models.CASCADE)
    slide_number = models.IntegerField()

    class Meta:
        order_with_respect_to = 'slide_number'

class NormalAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    slide = models.ForeignKey(Slide, on_delete=models.CASCADE)

class Choice(models.Model):    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    slide = models.ForeignKey(Slide, on_delete=models.CASCADE)
    choice_number = models.IntegerField()

    class Meta:
        ordering = ['choice_number']

class ChoiceAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

class OrderAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    order = models.IntegerField()

class QuestionScores(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.TextField(max_length=10)

class Score(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)