from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .models import CustomUserModel, TagModel, HistoryModel
from django.urls import reverse_lazy
from django.views import View
from .forms import HistoryCreateForm, TagCreateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class SignupView(View):
    '''サインアップ'''

    def get(self, request, *args, **kwargs):
        return render(request, 'history/signup.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        # ユーザーを追加
        try:
            CustomUserModel.objects.get(username=username)
            return render(request, 'history/signup.html', {'error': 'このユーザー名は既に登録されています．'})
        except:
            user = CustomUserModel.objects.create_user(username, '', password)
            # 新しいユーザーが作成されたタイミングで並び順モデルに新しいデータを追加
            # HowtoOrder.objects.create(user_name=username)
            return redirect('login')


class LoginView(View):
    '''ログイン'''

    def get(self, request, *args, **kwargs):
        return render(request, 'history/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')


def logoutfunc(request):
    logout(request)
    return redirect('login')


class HistoryCreateView(View):
    def get(self, request, *args, **kwargs):
        username = request.user.username
        tags = TagModel.objects.filter(username=username)
        context = {
            'form': HistoryCreateForm(),
            'username': username,
            'tags': tags,
        }
        return render(request, 'history/create_post.html', context)

    def post(self, request, *args, **kwargs):
        request_copy = request.POST.copy()
        request_copy['question'] = request_copy['question'].rstrip().lstrip()
        request_copy['answer'] = request_copy['answer'].rstrip().lstrip()
        request_copy['char_num'] = len(request_copy['answer'])
        form = HistoryCreateForm(request_copy)
        if form.is_valid():
            form.save()
            print('ok')
            return redirect('list')
        else:
            print('failed')
            return redirect('create_his')


class HistoryListView(ListView):
    # memo LoginRequiredMixinとListViewの順番を入れ替えるとうまくいかない
    '''タスクの一覧を表示'''

    def get(self, request):
        # ログイン中のユーザー名を取得
        username = request.user.username
        histories = HistoryModel.objects.filter(username=username)
        print(username)

        context = {
            'username': username,
            'histories': histories,
        }
        return render(request, 'history/list.html', context)


class HistoryDetailView(DetailView):
    '''タスクの詳細を表示'''
    template_name = 'history/detail_his.html'
    model = HistoryModel


class TagCreateView(View):
    def get(self, request, *args, **kwargs):
        username = request.user.username
        context = {
            'form': TagCreateForm(),
            'username': username,
        }
        return render(request, 'history/create_tag.html', context)

    def post(self, request, *args, **kwargs):
        form = TagCreateForm(request.POST)
        if form.is_valid():
            form.save()
            print('ok')
            return redirect('list')
        else:
            print('failed')
            return redirect('create_his')
