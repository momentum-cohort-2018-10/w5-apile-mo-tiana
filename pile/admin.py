from django.contrib import admin
from pile.models import Post, Comment, Favorite


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields: {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ("comment", "author",)
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Favorite)