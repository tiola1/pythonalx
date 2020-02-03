from django.urls import path
from polls.views import index, question_details, question_list, vote

app_name = "polls"

urlpatterns = [
    path("", index, name="index"),
    path('pytanie/', question_list, name="questions-list"),
    path('pytanie/<id>', question_details, name="details")
    path('pytanie/<id>/vote', vote, name="vote")
]

