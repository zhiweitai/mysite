from django.shortcuts import render
from django.http import HttpResponse
#from django.template import RequestContext, loader
from django.shortcuts import render
# Create your views here.
from .models import Question


def index(request):
    last_question_list = Question.objects.order_by('-pub_date')[0:5]
    """
    template = loader.get_template('polls/index.html')
    context = RequestContext(request,{
        'last_question_list': last_question_list,
    })
    return HttpResponse(template.render(context))
    """
    context = {'last_question_list': last_question_list}
    return render(request,'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." %question_id)

def results(request, question_id):
    response = "You're looking at the requests of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)