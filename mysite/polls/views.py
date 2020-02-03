from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from django.urls import reverse

from polls.models import Question


def index(request):
    return HttpResponse("Hello world! That's polls index")


# def questions_list(request):


def question_details(request, id):
    q = Question.objects.get(id=id)

    return render(
        request,
        "details.html",
        {"question": q}
    )


def question_list(request):
    qs = Question.objects.get(id=id)

    return render(
        request,
        "list.html",
        {"questions": qs}
    )

def vote(request, id):
    question = Question.objects.get(pk=id)
    choice_id=request.POST.get('choice')
    if choice_id:
        choice = question.choices.get(id=choice_id)
        choice.votes += 1
        choice.save()
    else:
        return render(request, "details.html,"
                               " {"question":question"
        {}
    print("Odbyło się głosowanie")

    return HttpResponseRedirect(reverse"")