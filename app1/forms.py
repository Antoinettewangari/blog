from django import forms
from .models import Blogs,Comment
from django.contrib.auth.models import User



class BlogsForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['photos','title','post']



class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['email','username','password']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment']