from django.db import models
from django.contrib.auth.models import User
from pages.models import Category


class UserProfile(models.Model):
    phone = models.CharField(max_length=10, blank=True, null=True)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    type_account = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='usercategory', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userprofile')
    
    def __str__(self):
        return self.user.username
    
    