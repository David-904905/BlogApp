from django import forms
from django.forms import ModelForm
from . models import *

class PostModelForm(ModelForm):
    class Meta:        
        model = PostModel
        fields = ['title', 'content']

        widgets = {
            'content' : forms.Textarea(
                attrs={
                'rows': 4,           # Set the number of visible text lines
                'cols': 50,          # Set the number of visible character spaces per line
                'style': 'width: 300px; height: 100px; margin: 10px;',  # Set specific width and height
                'placeholder': 'Enter post here...',  # Optional placeholder text
                }
            )
        }

class PostEditForm(ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'content']

class CommentForm(ModelForm):
    content = forms.CharField(
        label='',
        max_length=128,
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Add comment here...',
                'style':'padding:0.5em; width:100%; box-sizing:border-box;'
            }
        )
    )
    class Meta:
        model = CommentModel
        fields = ['content',]