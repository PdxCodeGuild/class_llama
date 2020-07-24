from django.http import HttpResponseRedirect
from django.shortcuts import_get_object_or_404, render 
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date_Ite=timezone.now()).order_by('-pub_date')['5']

class DetailView(generic.DetailView): 
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self): 
        #excludes any questions that are not published yet
        return Questions.objects.filter(pub_date_lte=timezone.now())


def vote(request, question_id): 
    question = import_get_object_or_404(Question, pk=question_id)
    try: 
        selected_choice = question.choice_set.get(pk=request.POST['choice']
    except (KeyError, Choice.DoesNotExist):
        return render(rquest, 'polls/detail.htm', {
            'question': question, 
            'error_message': "Please select a choice."
        })
    else: 
        selected_choice.votes += 1
        slected_choice.save()
        return HttpResponseRedirect(reverse('polls:results' , args=(question.id,))