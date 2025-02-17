from django.db import models
from enum import Enum

# Create your models here.
class ChoiceEnum(Enum):
    DISAGREE = 0, 'Disagree'
    AGREE = 1, 'Agree'
    

class Question(models.Model):
    text = models.CharField(max_length=200)
    index = models.IntegerField()

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField(choices=[(tag.value[0], tag.value[1]) for tag in ChoiceEnum])
    incorrect_answer_text = models.CharField(max_length=1000)

    def __str__(self):
        return str((self.question, self.answer, self.incorrect_answer_text))