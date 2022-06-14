from turtle import title
from django.db import models

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now=True)
    

