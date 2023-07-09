from django.db import models
# from django_resized


class User(models.Model):
    # id = AutoField()
    username = models.CharField(max_length=50)
    email = models.EmailField()
    homepage = models.URLField(default="", null=True)
    avatar = models.ImageField(height_field=320, width_field=240)
    # avatar =
    password = models.CharField(max_length=30)


class Post(models.Model):
    # id = AutoField()
    user_id = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="Anonymus", null=True)
    date = models.DateTimeField()
    file = models.FileField(upload_to="attachments/")
    text = models.CharField(max_length=200)
    prev_post = models.PositiveIntegerField(default="root")
