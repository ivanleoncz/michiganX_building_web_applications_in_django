from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
            'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def owner(request):
    return HttpResponse("Hello, world. 842efe84 is the polls index.")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice = request.POST.get('choice')

    if question and choice:
        selected_choice = question.choice_set.get(pk=choice)
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    else:
        return render(request, 'polls/detail.html',
                {
                    'question': question,
                    'error_message': "You didn't select a choice."
                })
