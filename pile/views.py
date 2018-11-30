from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
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
     favorites = Favorite.objects.all()
     favorite_posts = []
     if request.user.is_authenticated:
          favorite_posts = request.user.favorite_posts.all()
     return render(request, 'index.html', {
         'posts': posts,
         'favorites': favorites,
         'favorite_posts': favorite_posts,

     })

def post_detail(request, slug):
     post = Post.objects.get(slug=slug)
     form = CommentForm(request.POST)
     comments = Comment.objects.all()
     return render(request, 'posts/post_detail.html', {
          'post': post, 
          'comment_form': form,
          'comments': comments,
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
     # comment_form = CommentForm(request.POST)
     if comment_form.is_valid():
          comment = form.save(commit=False)
          comment.author = request.user
          Comment.objects.create(user=user, comment=comment)
          comment.save()
          return redirect("post_detail", slug=slug)
     else:
          form = form_class()

     return render(request, 'index.html', {
          "form": form,
     })

def favorites_list(request):
     posts = request.user.favorite_posts.all()
     return render_post_list(request, 'my favorite posts', posts)

def render_post_list(request, header, posts):
     posts = posts.annotate(num_of_favorites=Count('favorites'))
     favorite_posts = []
     if request.user.is_authenticated:
          favorite_posts = request.user.favorite_posts.all()
     posts = posts.orderby('created_at')
     return render(request, 'index.html',{
          "header": header,
          "posts": posts,
          "favorite_posts": favorite_posts
     })

@require_POST
def change_favorite(request, post_id):
     if request.method == "POST":

          post = Post.objects.get(pk=post_id)
          


          if post in request.user.favorite_posts.all():
               post.favorites.get(user=request.user).delete()
               message = "That's none of my business"
          
          else: 
               post.favorites.create(user=request.user)
               message = "This is my cup of tea!"

     messages.add_message(request, messages.INFO, message)
     return redirect(f'/#post-{post.pk}')

