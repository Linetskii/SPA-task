"""SPA models"""
from django.db import models
from django_resized import ResizedImageField
from django_bleach.models import BleachField


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
    text = BleachField()
    prev_post = models.PositiveIntegerField(default=0)
    n_answers = models.PositiveIntegerField(default=0)
    # rating = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.prev_post != 0:
            prev = Post.objects.filter(id=self.prev_post)
            print(prev[0].n_answers)
            prev.update(n_answers=(prev[0].n_answers + 1))
        super().save(*args, **kwargs)
