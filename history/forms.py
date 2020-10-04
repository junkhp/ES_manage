from django import forms
from .models import HistoryModel, TagModel


class HistoryCreateForm(forms.ModelForm):
    '''ポストを作成するフォーム'''
    class Meta:
        model = HistoryModel
        fields = ('question', 'answer', 'tags', 'open_info',
                  'company', 'state', 'username', 'char_num')


class TagCreateForm(forms.ModelForm):
    '''タグを作成するフォームクラス'''
    class Meta:
        model = TagModel
        fields = ('tag_name', 'username')


class UpdateForm(forms.ModelForm):
    '''ポストを修正するフォーム'''
    class Meta:
        model = HistoryModel
        fields = ('question', 'answer', 'tags', 'open_info',
                  'company', 'state')
