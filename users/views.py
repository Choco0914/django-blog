from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from .forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail


def logout_view(request):
    """사용자 로그아웃"""
    logout(request)
    return HttpResponseRedirect(reverse('my_blog:index'))

def register(request):
    """새 사용자를 등록한다."""
    if request.method != 'POST':
        # 빈 폼을 보여준다.
        form = UserCreationForm()
    else:
        # 전송받은 폼을 처리한다.
        form =UserCreationForm(data = request.POST)
        if form.is_valid():
            new_user = form.save()

            # 가입후 가입했다는 메일을 보내준다.
            # sand_mail(subject, message, from_email, to_list, fail_silently=True)
            subject = 'my_blog에 가입하신걸 환영합니다'
            message = 'https://choco-blog.herokuapp.com/ 에서 무엇이든 포스트해보세요!'
            from_email = settings.EMAIL_HOST_USER
            to_list = [new_user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True )

            # 사용자를 로그인시키고 홈페이지로 리다이렉트한다.
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('my_blog:index'))

    context = {'form' : form}
    return render(request, 'users/register.html', context)
