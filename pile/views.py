from django.shortcuts import render, redirect
from pile.models import Post, Comment, Favorite
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    # posts = Post.objects.all()
    return render(request, 'index.html'
    # , {'posts': posts,}
    )