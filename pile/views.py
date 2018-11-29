from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.views import login_required
from django.http import Http404
from pile.models import Post, Comment, Favorite
from django.contrib.auth import authenticate, login
from django.db.models import Count
from django.contrib import messages
from pile.forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {
         'posts': posts,}
    )

def post_detail(request, slug):
     post = Post.objects.get(slug=slug)
     return render(request, 'posts/post_detail.html', {
          'posts': posts,}
     )

@login_required
def create_post(request):
     form_class = PostForm
     if request.method == "POST":
          form = form_class(request.POST)
          if form.is_valid():
               post = form.save(commit=False)
               post.user = request.user
               post.slug = slugify(post.name)
               post.save()
               return redirect("post_detail", slug=post.slug)
     else:
          form = form_class()

     return render(request, 'posts/create_post.html', {
          "form": form,
     })

def edit_post(request, slug):
     post = Post.objects.get(slug=slug)
     if post.user != request.user:
          raise Http404

     form_class = PostForm

     if request.method == 'POST':
          form = form_class(data=request.POST, instance=post)
          if form.is_valid():
               form.save()
               return redirect("post_detail", slug=post.slug)
     else:
          form = form_class(instance=post)
          return render(request, 'posts/edit_post.html', {
               "post": post,
               "form": form,
          })