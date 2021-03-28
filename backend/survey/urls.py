from django.urls import path, include
from rest_framework import routers

from .api import SurveyViewSet, AnswersAPI

router = routers.SimpleRouter()
router.register(r'surveys', SurveyViewSet)

# /api/
urlpatterns = [
    path('', include(router.urls)),
    path('get_user_answers/', AnswersAPI.as_view()),
]
