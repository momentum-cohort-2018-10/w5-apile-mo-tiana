from django.forms import ModelForm
from pile.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'link', 'description')