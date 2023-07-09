from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.add_user, name="add_user"),
    path("", views.add_post, name="add_post"),
    path("", views.load_posts, name="load_posts"),
]