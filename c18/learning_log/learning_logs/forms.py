from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    '''Form to Topic model'''
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}