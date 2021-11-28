from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


def index(request):
    myname = "Tran Long"
    taisan = ["Dien thoai", "May Tinh", "May Bay", "Nhieu tien"]
    context = {"name": myname, "taisan": taisan}
    return render(request, "polls/index.html", context)


def viewlist(request):
    # get all
    # list_question  = Question.objects.all()
    # list_question = get_object_or_404(Question, pk = 1)
    list_question = Question.objects.all()
    return render(request, "polls/quetion_list.html", {"list_question": list_question})


def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html", {"q": q})


def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        dulieu = request.POST["choice"]
        c = q.choice_set.get(pk=dulieu)
    except:
        HttpResponse("Loi khong co choi")
    c.vote = c.vote + 1;
    c.save()
    return render(request, "polls/result.html", {"q": q})