from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm


# Create your views here.

class IndexClass(View):
    def get(self, request):
        return HttpResponse('<h1> xin chao </h1>')


class LoginClass(View):
    def get(self, request):
        return render(request, 'Login/Login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        my_user = authenticate(username=username, password=password)
        if my_user is None:
            return HttpResponse('User Does Not Exit')
        login(request, my_user)

        return render(request, 'Login/success.html')


class ViewUser(LoginRequiredMixin, View):
    login_url = 'login/'

    def get(self, request):
        return HttpResponse('<h1>This is the view User</h1>')


# require login
@decorators.login_required(login_url='login/')
def view_product(request):
    return HttpResponse('xem san pham')


class AddPost(LoginRequiredMixin,View):
    login_url = 'login/'
    def get(self, request):
        f = PostForm()
        context = {
            'fm': f
        }
        return render(request, 'Login/add_post.html', context)
    def post(selfs, request):
        f = PostForm(request.POST)
        if not f.is_valid():
            return HttpResponse('May nhap sai du lieu roi')
        #cache reload tu database user
        #in quen
        print(request.user.get_user_permissions())
        if(request.user.has_perm('Login.add_post')):
            f.save()
        else:
            return HttpResponse('may khong co quen ')
        return HttpResponse('ok')