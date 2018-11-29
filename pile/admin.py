from django.contrib import admin
from pile.models import Post, Comment, Favorite


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields: {"slug": ("title",)}

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Favorite)