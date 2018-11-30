from django.forms import ModelForm
from pile.models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'link', 'description',)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

