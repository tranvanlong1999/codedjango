from django.shortcuts import render
from django.http import  HttpResponse
from .forms import PostForm
from .forms import SendEmail
from django.views import View
# Create your views here.


class IndexClass(View):
    def get(self, request):
        ketqua = 12343432
        return HttpResponse(ketqua)


class ClassSaveNews(View):
    def get(self, request):
        a = PostForm()
        return render(request, 'news/add_new.html', {'f': a})
    def post(self,request):
        g = PostForm(request.POST)
        if(g.is_valid()):
            g.save()
            return HttpResponse('luu ok')
        else:
            return HttpResponse('Khong dc validate')

def email_view(request):
    b = SendEmail()
    return render(request, 'news/email.html' , { 'f' : b})


def process(request):
    if request.method == "POST":
        m = SendEmail(request.POST)
        if(m.is_valid()):
            tieude = m.cleaned_data['title']
            cc = m.cleaned_data['cc']
            noidung = m.cleaned_data['content']
            email  = m.cleaned_data['email']
            # context = {
            #     'tieude' : tieude,
            #     'cc' :cc,
            #     'noidung':noidung,
            #     'email':email
            # }
            context2 ={'emailData' : m }
            return render(request ,'news/print_email.html' , context2)
        else:
            return HttpResponse('form not vaild')
    else:
        return HttpResponse('Do not post method')