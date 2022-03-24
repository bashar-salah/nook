from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='category', blank=True, null=True)
    
    def __str__(self):
        return self.name


class About(models.Model):
    description = models.TextField(blank=True, null=True)


class Addwork(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    photo = models.ImageField(upload_to='works', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='addworkcategory', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addworkuser', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-id',)


class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    photo = models.ImageField(upload_to='blog', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bloguser', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-date',)
    

class CommentsBlog(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    registeruser = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='commentuser')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True, related_name='commentblog')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-date',)
        

class Contect(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    message = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    
    def __str__(self):
        return self.name