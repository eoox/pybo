from pybo.models import Question
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    #question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, '../templates/pybo/question_detail.html', context)