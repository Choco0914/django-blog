from django import forms

from .models import Topic, Content, Comment

class TopicForm(forms.ModelForm):
    """주제의 폼을 정의한다"""
    class Meta:
        model = Topic
        fields = ['text', 'public']
        labels = {'text': '', 'public': '주제를 공개하려면 체크해주세요'}

class ContentForm(forms.ModelForm):
    """주제에 맞는 내용의 폼을 정의한다."""
    class Meta:
        model = Content
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}

class CommentForm(forms.ModelForm):
    """댓글의 폼을 정의한다"""
    class Meta:
        model = Comment
        fields = ['text']
        lavels = {'text': '',}
