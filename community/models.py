from django.db import models
from pages.models import Category
from datetime import datetime
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    category = models.OneToOneField(Category, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name
    

class Messages(models.Model):
    message = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    hide = models.BooleanField(default=False, blank=True, null=True)
    hide_id  =models.CharField(max_length=100, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
        # return self.hide
