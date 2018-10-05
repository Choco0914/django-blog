from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


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
            # 사용자를 로그인시키고 홈페이지로 리다이렉트한다.
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('my_blog:index'))

    context = {'form' : form}
    return render(request, 'users/register.html', context)
