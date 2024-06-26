from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def say_hello(request):
    return render(request, 'hello.html', {'name':'Sabari'})


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html',
                  {'posts':posts})