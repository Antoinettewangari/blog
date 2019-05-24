from django.shortcuts import render, get_object_or_404,redirect
from .models import Blogs
from django.views.generic import ListView
from .forms import BlogsForm


# Create your views here.

class BlogPosts(ListView):
    model = Blogs
    template_name = 'app1/index.html'
    context_object_name = 'profiles'

def add_blog(request):
    form = BlogsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        blog=form.save(commit=False)
        blog.photos=request.FILES['photos']



        blog.save()
        return redirect('app1:index')
    return render(request,'app1/add_blog.html',{'form':form})


def index(request):

    return render(request,'app1/index.html')
