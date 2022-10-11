
from django.forms import ModelForm
from .models import Comment, Post
from django import forms


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'contenido','active')

class PostForm(ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2,'placeholder':'¿que quieres postear?'}), required=True)

    class Meta:
        model = Post
        fields = ['title','content']