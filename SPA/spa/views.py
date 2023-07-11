"""Views for SPA"""
import asyncio
from datetime import datetime, timezone
from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import User, Post


def index(request):
    """The only one page"""
    if request.method == "POST":
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            print('form validated')
            asyncio.run(add_user(form.cleaned_data))
            # user_id = asyncio.run(get_user_id(form.cleaned_data.get('username')))
            asyncio.run(add_post(form.cleaned_data, User.objects.get(username=form.cleaned_data.get('username')).id))
            return redirect("index")
        print(form.errors)
    form = MessageForm()
    print('index_load')
    return render(request, "spa/index.html", {"form": form})


async def add_post(form, user_id, prev_post=0):
    """Add post to database"""
    print('adding post')
    await Post.objects.acreate(
        user_id=user_id,
        date=datetime.now(tz=timezone.utc),
        file=form.get('attachment'),
        text=form.get('text'),
        prev_post=prev_post,
    )


async def add_user(form):
    """Add user to database"""
    print('adding user')
    await User.objects.acreate(
        username=form.get('username'),
        email=form.get('email'),
        homepage=form.get('homepage'),
        avatar=form.get('avatar'),
        password=form.get('password'),
    )


async def load_posts(n):
    """Load posts from database"""
    print('load messages...')
    await Post.objects.aall()[n*25:(n*25 + 25)]  # .order_by()


async def get_user_id(username):
    await User.objects.aget(username=username)
