from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .models import CustomUserModel, TagModel, HistoryModel
from django.urls import reverse_lazy, reverse
from django.views import View
from .forms import HistoryCreateForm, TagCreateForm, UpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Create your views here.


class SignupView(View):
    '''サインアップ'''

    def get(self, request, *args, **kwargs):
        return render(request, 'history/signup.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        # ユーザーを追加
        if CustomUserModel.objects.filter(username=username).exists():
            return render(request, 'history/signup.html', {'error': 'このユーザー名は既に登録されています．'})
        else:
            CustomUserModel.objects.create_user(username, '', password)
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
            return redirect('list', username=username)
        else:
            return redirect('login')

# ログアウト関数


def logoutfunc(request):
    logout(request)
    return redirect('login')


class HistoryCreateView(View):
    '''質問と回答(post)を作成する'''

    def get(self, request, *args, **kwargs):
        login_username = request.user.username
        tags = TagModel.objects.filter(username=login_username)
        num_tags = len(tags)

        # ポスト作成画面(templates/history/create_post.html)にて一度に表示するタグ数の上限
        # タグの数が上限より多い時はスクロールになる
        max_num_tags = 10
        context = {
            'form': HistoryCreateForm(),
            'login_username': login_username,
            'tags': tags,
            # タグの数に応じてpost画面のタグの表示数を変更
            'len_tags': min(num_tags, max_num_tags),
        }
        return render(request, 'history/create_post.html', context)

    def post(self, request, *args, **kwargs):
        login_username = request.user.username

        # 回答の文字数を取得
        # 回答の前後にスペースがある場合，それらを削除してから文字数を取得
        request_copy = request.POST.copy()
        request_copy['question'] = request_copy['question'].rstrip().lstrip()
        request_copy['answer'] = request_copy['answer'].rstrip().lstrip()
        request_copy['char_num'] = len(request_copy['answer'])
        form = HistoryCreateForm(request_copy)
        if form.is_valid():
            form.save()
            print('ok')
            return redirect('list', username=login_username)
        else:
            print('failed')
            return redirect('create_his')


# class Userlist(ListView):
#     model = HistoryModel
#     slug_field = "username"
#     slug_url_kwarg = "username"
#     template_name = 'history/list.html'

#     def get_object(self):
#         object = get_object_or_404(HistoryModel, username=self.kwargs.get("username"))
#         if self.request.user.username == object.username:
#             return object
#         else:
#             print("you are not the owner!!")


class HistoryListView(ListView):
    # memo LoginRequiredMixinとListViewの順番を入れ替えるとうまくいかない
    '''タスクの一覧を表示'''

    def get(self, request, username):
        # ログイン中のユーザー名を取得
        login_username = request.user.username
        if login_username == '':
            login_username = 'ゲスト'

        # print('---------------')
        # print(login_username)
        # print(type(login_username))
        # print(len(login_username))
        # print('---------------')

        # ゆーざーDBに登録されていないユーザ名がリクエストされることも想定される
        # この方法がベストかはわからないがとりあえず．
        # ユーザーが存在していないときの処理
        if CustomUserModel.objects.filter(username=username).count() == 0:
            context = {
                'username': username,
                'login_username': login_username,
            }
            return render(request, 'history/list_not_exist.html', context)

        # ログインしていない人のポストを見るときには制限をかける
        # ログインしているとき
        if login_username == username:
            histories = HistoryModel.objects.filter(username=username)

            context = {
                'username': username,
                'histories': histories,
                'login_username': login_username
            }
            return render(request, 'history/list.html', context)

        # ログインしていないとき
        else:
            # memo:カンマで区切るとAND検索
            histories = HistoryModel.objects.filter(username=username, open_info='public')
            context = {
                'username': username,
                'histories': histories,
                'login_username': login_username,
            }
            return render(request, 'history/list_not_login.html', context)


class HistoryDetailView(DetailView):
    '''タスクの詳細を表示'''
    template_name = 'history/detail_his.html'
    model = HistoryModel


class HistoryDeleteView(DeleteView):
    '''タスクを削除'''

    template_name = 'history/delete_post.html'
    model = HistoryModel
    # success_url = reverse_lazy('list', username=login_username)

    def get_success_url(self):
        print(self.request.user.username)
        return reverse('list', kwargs={'username': self.request.user.username})


class HistroyUpdateView(View):
    '''ポストを修正'''

    def get(self, request, pk, *args, **kwargs):
        login_username = request.user.username
        post = HistoryModel.objects.get(pk=pk)
        form = UpdateForm(instance=post)
        tags = TagModel.objects.filter(username=login_username)
        print(post)
        context = {
            'form': form,
            'login_username': login_username,
            'tags': tags,
            # タグの数に応じてpost画面のタグの表示数を変更，タグが10個以上の場合はスクロール
            'len_tags': min(len(tags), 10),
        }
        return render(request, 'history/update_post.html', context)

    def post(self, request, pk, *args, **kwargs):
        login_username = request.user.username
        post = HistoryModel.objects.get(pk=pk)
        form = UpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('list', username=login_username)
        else:
            return redirect('update')


class TagCreateView(View):
    '''タグを作成するview'''

    def get(self, request, *args, **kwargs):
        login_username = request.user.username
        tags = TagModel.objects.filter(username=login_username)
        num_tags = len(tags)
        context = {
            'form': TagCreateForm(),
            'login_username': login_username,
            'tags': tags,
            'num_tags': num_tags,
        }
        return render(request, 'history/create_tag.html', context)

    def post(self, request, *args, **kwargs):
        login_username = request.user.username
        form = TagCreateForm(request.POST)
        if form.is_valid():
            form.save()
            print('ok')
            return redirect('list', username=login_username)
        else:
            print('failed')
            return redirect('create_tag')


class SearchUserView(View):
    '''ユーザー検索'''

    def get(self, request, *args, **kwargs):
        search_user = self.request.GET.get('search_username')
        login_username = request.user.username
        if login_username == '':
            login_username = 'ゲスト'
        context = {
            'login_username': login_username,
            'search_user': search_user,
        }
        if CustomUserModel.objects.filter(username=search_user).exists():
            context['error'] = False
        else:
            context['error'] = True
        return render(request, 'history/search_user.html', context)
