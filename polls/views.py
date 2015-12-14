from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import RequestContext, loader
from django.shortcuts import render
from django.core.urlresolvers import reverse
# Create your views here.
from .models import Question, Choice


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
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    response = "You're looking at the requests of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    p = get_object_or_404(Question, question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':p,
            'error_message':"You didn't select a choice",
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args={p.id, }))