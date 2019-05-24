from django import forms
from .models import Blogs


class BlogsForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['name','photos','title','post']