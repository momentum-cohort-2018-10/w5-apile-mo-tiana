from django.contrib import admin
from pile.models import Post, Comment, Favorite

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Favorite)