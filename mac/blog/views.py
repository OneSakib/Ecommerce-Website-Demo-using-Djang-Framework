from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'blog/index.html')


def about(request):
    return render(request,'blog/about.html')


def contact(request):
    return render(request,'blog/contact.html')


def tracker(request):
    return render(request,'blog/tracker.html')


def search(request):
    return render(request,'blog/search.html')


def productview(request):
    return  render(request,'blog/productview.html')


def checkout(request):
    return render(request,'blog/checkout.html')

