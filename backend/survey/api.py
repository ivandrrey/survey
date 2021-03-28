from rest_framework import viewsets, permissions, views
from rest_framework.generics import get_object_or_404
from django.http import JsonResponse
from datetime import datetime

from survey.models import Survey, SurveyResult, Question
from survey.serializers import SurveySerializer, SurveyListSerializer


# api/surveys/ - список актуальных
# api/surveys/<int:survey_id>/ - отдельный опрос по id
class SurveyViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]

    queryset = Survey.objects.filter(end_date__gte=datetime.now())
    serializer_classes = {
        'retrieve': SurveySerializer,
        'list': SurveyListSerializer,
    }
    lookup_field = 'id'

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, SurveyListSerializer)

    def get_object(self):
        return get_object_or_404(self.queryset, id=self.kwargs.get(self.lookup_field))

    def post(self, request, id):
        survey = self.get_object()
        user_id = self.request.data.get('user_id', None)
        answers = self.request.data.get('answers', {})

        if not isinstance(answers, dict):
            return JsonResponse({'detail': 'Неверный формат данных "answers".'}, status=400)
        if user_id is None or isinstance(user_id, int):
            result = SurveyResult(user_id=user_id, survey_id=survey.id, answers=answers)
            result.save()
            return JsonResponse({'detail': 'Ответы сохранены.'}, status=200)
        else:
            return JsonResponse({'detail': 'Неверный формат данных "user_id".'}, status=400)


# 'get_user_answers/' - список опросников пользователя и его ответы в них
class AnswersAPI(views.APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        user_id = self.request.GET.get('user_id', None)
        survey_id = self.request.GET.get('survey_id', None)
        user_results = SurveyResult.objects.filter(user_id=user_id)
        if survey_id is not None:
            user_results = user_results.filter(survey_id=survey_id)

        response = []
        for result in user_results.all():
            questions = dict(Question.objects.filter(id__in=result.answers.keys()).values_list('id', 'text').all())
            answers = {}
            for questions_id in questions.keys():
                answers[questions_id] = {'text': questions[questions_id], 'answer': result.answers[str(questions_id)]}
            response.append({'survey_id': result.survey_id, 'answers': answers})

        return JsonResponse(response, status=200, safe=False)
