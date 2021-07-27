from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1 style='text-align:center';>Hello Welcome to this Website</>")
