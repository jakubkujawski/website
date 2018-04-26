from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# this is our first view, it takes a request from the user and returns some simple text, without html
def music_home(request):
    return render(request, "music/home.html")

def music_download(request):
    return HttpResponse("Hello, you can download music here.")

def music_favourite(request):
    return HttpResponse("Hello, your favourite music is here.")