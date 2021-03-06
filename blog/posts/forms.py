from django.forms import ModelForm
from .models import Post


class Form(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'created_at')
