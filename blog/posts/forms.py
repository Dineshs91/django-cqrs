from django.forms import ModelForm

from posts.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']