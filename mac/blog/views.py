from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost


# Create your views here.
def index(request):
    post = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'post': post})


def blogpost(request, myid):
    post = BlogPost.objects.filter(post_id=myid)[0]
    return render(request, 'blog/blogpost.html', {'post': post})
