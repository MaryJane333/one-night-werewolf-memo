from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import CreateName, CreateNumber
from .models import NameModel, NumberModel

# Create your views here.

def list_func(request):
    name_list = NameModel.objects.filter(username=request.user)
    
    try:
        number_list = NumberModel.objects.get(username=request.user)   
        return render(request, 'list.html', {'name_list':name_list, 'number_list':number_list})
    except ObjectDoesNotExist: # NumberModelがない時の処理
        return redirect('create_number')

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
            return render(request, 'done_sign_up.html', {})
        except IntegrityError:
            return render(request, 'sign_up.html', {'error':'このユーザー名は既に使われています。'})
    return render(request, 'sign_up.html')

class Delete(DeleteView):
    template_name = 'delete.html'
    model = NameModel
    success_url = reverse_lazy('list')

class NameCreate(CreateView):
    model = NameModel
    fields = ('name', 'username')
    success_url = reverse_lazy('list')
    def get(self, request):
        initial_dict = dict(name='', username=self.request.user)
        form = CreateName(request.GET or None, initial=initial_dict)
        return render(request, 'create.html', dict(form=form))

class NameUpdate(UpdateView):
    template_name = 'update_name.html'
    model = NameModel
    fields = ('name', 'username')
    success_url = reverse_lazy('list')

class NumberCreate(CreateView):
    model = NumberModel
    fields = ('villager', 'fortune_teller', 'thief', 'werewolf', 'madman', 'username')
    success_url = reverse_lazy('list')
    def get(self, request):
        initial_dict = dict(villager=0, fortune_teller=0, thief=0, werewolf=0, madman=0, username=self.request.user)
        form = CreateNumber(request.GET or None, initial=initial_dict)
        return render(request, 'create_number.html', dict(form=form))

class NumberUpdate(UpdateView):
    template_name = 'update_number.html'
    model = NumberModel
    fields = ('villager', 'fortune_teller', 'thief', 'werewolf', 'madman')
    success_url = reverse_lazy('list')
