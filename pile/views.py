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
          'post': post,
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

@require_POST
def change_favorite(request, post_id):
     post = Post.objects.get(pk=post_id)

     if post in request.user.favorite_posts.all():
          post.favorites.get(user=request.user).delete()
     else: 
          post.favorites.create(user=request.user)

     return redirect(f'/#post-{post.pk}')
