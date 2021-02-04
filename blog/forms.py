from django import forms
from .models import Post, Comment, Comment1

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment1
        fields = ('author', 'text',)
