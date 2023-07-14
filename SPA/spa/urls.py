from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("", views.add_user, name="add_user"),
    path("", views.add_post, name="add_post"),
    path("", views.load_posts, name="load_posts"),
    re_path("^answers/", views.answers, name="answers")
]
