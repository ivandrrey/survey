from rest_framework import serializers

from survey.models import Survey, Question, SurveyContent, SurveyResult


class SurveyContentSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='question.id')
    text = serializers.ReadOnlyField(source='question.text')
    question_type = serializers.ReadOnlyField(source='question.question_type')

    class Meta:
        model = SurveyContent
        fields = ('id', 'text', 'question_type')

    def to_representation(self, instance):
        output = super(SurveyContentSerializer, self).to_representation(instance)
        output['question_type'] = dict(Question.QUESTION_TYPES).get(output['question_type'], None)
        return output


class SurveySerializer(serializers.ModelSerializer):
    questions = SurveyContentSerializer(source='survey_questions', many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ('id', 'name', 'start_date', 'end_date', 'description', 'questions')


class SurveyListSerializer(serializers.ModelSerializer):
    questions = SurveyContentSerializer(source='survey_questions', many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ('id', 'name', 'start_date', 'end_date', 'description', 'questions')