from django.urls import path
from .views import SMS_APIView


urlpatterns = [
    path("TEST/", SMS_APIView.as_view(),name="NLP_TEST")
]