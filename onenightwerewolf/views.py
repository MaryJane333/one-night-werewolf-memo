from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import NameModel, NumberModel

# Create your views here.

def list_func(request):
    name_list = NameModel.objects.all()
    number_list = NumberModel.objects.get(username='bambook')
    return render(request, 'list.html', {'name_list':name_list, 'number_list':number_list})

def login_func(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

def logoutfunc(request):
    logout(request)
    return  redirect('login')

def sign_up_func(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'list.html', {'subscribe':'登録完了'})
        except IntegrityError:
            return render(request, 'sign_up.html', {'error':'このユーザー名は既に使われています。'})
    return render(request, 'sign_up.html')

class Delete(DeleteView):
    template_name = 'delete.html'
    model = NameModel
    success_url = reverse_lazy('list')

class NameCreate(CreateView):
    template_name = 'create.html'
    model = NameModel
    fields = ('name', 'username')
    success_url = reverse_lazy('list')

class NameUpdate(UpdateView):
    template_name = 'update_name.html'
    model = NameModel
    fields = ('name', 'username')
    success_url = reverse_lazy('list')

class NumberUpdate(UpdateView):
    template_name = 'update_number.html'
    model = NumberModel
    fields = ('villager', 'fortune_teller', 'thief', 'werewolf', 'madman')
    success_url = reverse_lazy('list')
