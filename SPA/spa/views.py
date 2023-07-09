import asyncio
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import User, Post


def index(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            add_post(form.cleaned_data)
            add_user(form.cleaned_data)
            return redirect("index")
    else:
        form = MessageForm()
    return render(request, "spa/index.html", {"form": form})


async def add_post(form, prev_post="root"):
    await Post.objects.acreate(
        user_id=User.objects.get(name=form.username).id,
        date=datetime.now(),
        file=form.attachment,
        text=form.text,
        prev_post=prev_post,
    )


async def add_user(form):
    await User.objects.acreate(
        username=form.username,
        email=form.email,
        homepage=form.homepage,
        avatar=form.avatar,
        password=form.password,
    )


async def load_posts(n):
    await Post.objects.aall()[n*25:(n*25 + 25)]  # .order_by()

# asyncio.run(load_posts(1))
