from django import forms
from .models import HistoryModel, TagModel


class HistoryCreateForm(forms.ModelForm):

    class Meta:
        model = HistoryModel
        fields = ('question', 'answer', 'tags', 'open_info',
                  'company', 'state', 'username', 'char_num')


class TagCreateForm(forms.ModelForm):

    class Meta:
        model = TagModel
        fields = ('tag_name', 'username')
