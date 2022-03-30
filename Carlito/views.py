from django.http import HttpResponse
from django.shortcuts import render 

from blog.models import Post

def index(request):
     posts = Post.objects.all() 
     # return HttpResponse("Hola Mundo")
     return render (request, 'index.html', {
          'posts':posts, 
     })

def about(request):
     return render (request, 'about.html', {})
