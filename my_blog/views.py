from django.shortcuts import render

def index(request):
    """블로그 홈페이지"""
    return render(request, 'my_blog/index.html')
