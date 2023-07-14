"""SPA models"""
from django.db import models
from django_resized import ResizedImageField


class User(models.Model):
    """User model"""
    # id = AutoField()
    username = models.CharField(max_length=50)
    email = models.EmailField()
    homepage = models.URLField(null=True)
    avatar = ResizedImageField(size=[320, 240], upload_to='img')
    password = models.CharField(max_length=30)


class Post(models.Model):
    """Message model"""
    # id = AutoField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()
    file = models.FileField(upload_to="attachments/")
    text = models.CharField(max_length=200)
    prev_post = models.PositiveIntegerField(default=0)
    rating = models.IntegerField(default=0)
