from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth.views import login_required
from django.http import Http404
from pile.models import Post, Comment, Favorite
from django.contrib.auth import authenticate, login
from django.db.models import Count
from django.contrib import messages
from pile.forms import PostForm, CommentForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
#     form = CommentForm(request.POST)
    return render(request, 'index.html', {
         'posts': posts,
          }
    )

def post_detail(request, slug):
     post = Post.objects.get(slug=slug)
     comment = Post.objects.get(comment)
     return render(request, 'posts/post_detail.html', {
     'post': post,
     'comment': comment,
     })

@login_required
def create_post(request):
     form_class = PostForm
     if request.method == "POST":
          form = form_class(request.POST)
          if form.is_valid():
               post = form.save(commit=False)
               post.author = request.user
               post.slug = slugify(post.title)
               post.save()
               return redirect("post_detail", slug=post.slug)
     else:
          form = form_class()

     return render(request, 'posts/create_post.html', {
          "form": form,
     })

def edit_post(request, slug):
     post = Post.objects.get(slug=slug)
     if post.author != request.user:
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

def create_comment(request):
     form_class = CommentForm
     if request.method == "POST":
          form = form_class(request.POST)
          if form.is_valid():
               comment = form.save(commit=False)
               comment.author = request.user
               # Comment.objects.create(user=user, comment=comment)
               comment.save()
               return redirect("posts/post_detail")
          else:
               form = form_class()
               return render(request, 'posts/post_detail.html', {
               "post": post,
               "comment": comment,
               "form": form,
          })
