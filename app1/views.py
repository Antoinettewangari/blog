from django.shortcuts import render, get_object_or_404,redirect
from .models import Blogs, Comment
from django.views.generic import ListView
from .forms import BlogsForm, UserForm, CommentForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

class BlogPosts(ListView):
    model = Blogs
    template_name = 'app1/index.html'
    context_object_name = 'profiles'

    def get_query(self):
        query=self.request.GET.get('q')
        if query:
            return Blogs.objects.filter(title__icontains=query)|Blogs.objects.filter(post__icontains=query)
        else:
            return Blogs.objects.all()




@login_required(login_url='app1:login')
def add_blog(request):
    form = BlogsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        blog=form.save(commit=False)
        blog.photos=request.FILES['photos']
        blog.user=request.user



        blog.save()
        return redirect('app1:index')
    return render(request,'app1/add_blog.html',{'form':form})

def comment(request,blog_id):
    form = CommentForm(request.POST or None,request.FILES or None)
    blog=get_object_or_404(Blogs,pk=blog_id)
    if form.is_valid():
        commentform= form.save(commit=False)
        commentform.com=blog

        commentform.save()
        return redirect('app1:index')
    return render(request, 'app1/comment.html', {'form': form})


def signup(request):
    form=UserForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user=form.save(commit=False)
        user.set_password(password)
        user.save()
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect('app1:index')

    return render(request,'app1/signup.html',{'form':form})




def delete_blog(request,blog_id):
    blogs=get_object_or_404(Blogs,pk=blog_id)
    blogs.delete()
    return redirect('app1:index')

def index(request):

    return render(request,'app1/index.html')


def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect('app1:index')
    return render(request,'registration/login.html')

def logout_user(request):
    logout(request)
    return redirect('app1:login')



def update_post(request,blog_id):
    blog=get_object_or_404(Blogs,pk=blog_id)
    form=BlogsForm(request.POST or None ,request.FILES or None,instance=blog)
    if form.is_valid():
        blog=form.save()
        return redirect('app1:index')



    return render(request,'app1/add_blog.html',{'form':form})









