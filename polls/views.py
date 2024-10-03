from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Question, Choice


# Create your views here.

def index(request):
    myname= "jenny"
    mylist = ["jen","lap",'abc',"not"]
    # Question.objects.all()
    list_ques =  Question.objects.all()

    context = {"name" : myname, "list" : mylist,"alludes": list_ques}
    return render(request, 'polls/index.html', context)
def list_choice(request,ques_id):
    list_view = get_object_or_404(Question,pk=ques_id)
    return render(request,'polls/detail_ques.html', {"choice": list_view})
def base(request):
    return render(request, 'polls/base.html')
def vote(request,ques_id):
    q = Question.objects.get(pk=ques_id)
    try:
     content = request.POST['choice']
     c= q.choice_set.get(pk=content)
    except:
     HttpResponse("ko cos choice")
    c.vote = c.vote + 1
    c.save()
    return render(request,'polls/result.html', {"obj": q})
