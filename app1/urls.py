from django.contrib import admin
from django.urls import path,include
from .import views


app_name='app1'

urlpatterns = [
    path('', views.BlogPosts.as_view(), name='index'),
    path('add-blog',views.add_blog,name='add-blog'),
    path('(?P<blog_id>[0-9]+)/delete-blog', views.delete_blog, name='delete-blog'),
    path('(?P<blog_id>[0-9]+)/comment', views.comment, name='comment'),
    path('(?P<blog_id>[0-9]+)/update-post', views.update_post, name='update-post'),
    path('signup', views.signup, name='signup'),

    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),

   ]
