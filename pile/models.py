from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    link = models.URLField(unique=False, blank=True)
    description = models.TextField()
    slug = models.SlugField(default=None, unique=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    favorited_users = models.ManyToManyField(to=User, through="Favorite", related_name="favorite_posts")

    # def __init__(self, title, author, link, description, slug, created_at, favorited_users):
    #     self.title = title
    #     self.author = author
    #     self.link = link
    #     self.description = description
    #     self.slug = slug
    #     self.created_at = created_at
    #     self.favorited_users = favorited_users

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
    new_comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Favorite(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='favorites')


    class Meta:
        unique_together = ('post', 'user',)

