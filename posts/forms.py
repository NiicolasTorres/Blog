
from django.forms import ModelForm
from .models import Comment
from dataclasses import  fields

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields ('name', 'name', 'content','active')