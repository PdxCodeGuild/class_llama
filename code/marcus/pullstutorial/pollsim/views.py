from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World!")


def detail(request, question_id):
    return HttpResponse(f"You are looking at poll number {question_id}")

def results(request, question_id):
    return HttpResponse(f"You are looking at the results for poll number {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You are voting on question number {question_id}")

