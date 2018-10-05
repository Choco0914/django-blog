from django import forms

from .models import Topic, Content

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
