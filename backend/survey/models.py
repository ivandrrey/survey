from django.db import models
from datetime import datetime
import jsonfield


class Survey(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    start_date = models.DateTimeField(blank=False, null=False, auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(blank=False, null=False, auto_now=False, auto_now_add=False)
    description = models.TextField(blank=True, null=True, max_length=1020)

    def __str__(self):
        return self.name

    def is_active(self):
        if self.end_date and datetime.now() < self.end_date:
            return False
        return True


class Question(models.Model):
    TEXT = 'TXT'
    CHOOSE_ONE = 'CO'
    CHOOSE_A_LOT = 'CAL'
    QUESTION_TYPES = (
        (TEXT, 'Ответ текстом'),
        (CHOOSE_ONE, 'Выбор одного варианта'),
        (CHOOSE_A_LOT, 'Выбор нескольких вариантов'),
    )

    text = models.TextField(blank=False, null=False, max_length=1020)
    question_type = models.CharField(max_length=255, choices=QUESTION_TYPES, default=TEXT)

    def __str__(self):
        return self.text


class SurveyContent(models.Model):
    survey = models.ForeignKey('Survey', on_delete=models.CASCADE, related_name='survey_questions')
    question = models.ForeignKey('Question', on_delete=models.DO_NOTHING)


class SurveyResult(models.Model):
    user_id = models.DecimalField(blank=True, null=True, max_digits=10000, decimal_places=0)
    survey = models.ForeignKey('Survey', on_delete=models.CASCADE)
    # данные в формате {question_id: answer(list/str)}
    answers = jsonfield.JSONField()
