from django.contrib import admin
from pile.models import Post, Comment, Favorite


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields: {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ("new_comment", "author",)

class FavoriteAdmin(admin.ModelAdmin):
    model = Favorite
    list_display = ('post', 'user',)

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Favorite, FavoriteAdmin)
