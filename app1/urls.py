from django.contrib import admin
from django.urls import path,include
from .import views


app_name='app1'

urlpatterns = [
    path('', views.BlogPosts.as_view(), name='index'),
    path('add-blog',views.add_blog,name='add-blog'),
]
