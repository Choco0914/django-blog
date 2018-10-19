from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserCreationForm(UserCreationForm):
    """유저 가입양식 정의"""
    first_name = forms.CharField(widget = forms.TextInput(
    attrs={'class': 'form-control', 'placeholder': 'First Name'}),
     max_length=32, help_text='First name', label='이름')

    last_name = forms.CharField(widget =
    forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
     max_length=32, help_text='Last name', label='성')

    email = forms.EmailField(widget = forms.EmailInput(attrs=
        {'class':'form-control', 'placeholder': 'Email',}),
         max_length=64, help_text='유효한 이메일 주소를 입력하세요',
         error_messages={'invalid': ("Email 이 비어있습니다")},)

    terms = forms.BooleanField(
        label =('My blog of service'),
        widget=forms.CheckboxInput(
            attrs={
                'required': 'True',
            }
        ),
        error_messages={
            'required':('당신의 My blog of service 에 대한 동의가 필요합니다. ')
        }
    )

    privacy = forms.BooleanField(
        label=('Privacy policy'),
        widget=forms.CheckboxInput(
            attrs={
                'required':'True',
            }
        ),
        error_messages={
            'required=':('당신의 Privacy policy 동의가 필요합니다.')
            }
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name',
         'last_name', 'email')
