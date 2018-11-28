from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.views import login_required
from pile.models import Post, Comment, Favorite
from django.contrib.auth import authenticate, login
from django.db.models import Count
from django.contrib import messages

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html'
     , {'posts': posts,}
    )