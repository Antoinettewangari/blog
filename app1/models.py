from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blogs(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    photos = models.ImageField()
    post = models.TextField(max_length=2000)

class Comment(models.Model):
    com=models.ForeignKey(Blogs,on_delete=models.CASCADE)
    comment=models.TextField(max_length=40)

