"""Views for SPA"""
import asyncio
from datetime import datetime, timezone
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import ListView
from .forms import MessageForm
from .models import User, Post


class IndexView(ListView):
    template_name = 'spa/index.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        return context

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if User.objects.get(username=username).password != password:
                pass
            user = asyncio.run(add_user(form.cleaned_data))
            pp = int(form.cleaned_data.get('prev_post'))
            asyncio.run(add_post(form.cleaned_data, User.objects.get(username=username).id, pp))
            return redirect('index')
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)


def answers(request):
    pp = int(request.GET.get('prev_post'))
    answers = Post.objects.prefetch_related("user").filter(prev_post=pp).values('id', 'date', 'file', 'text', 'user__username', 'user__email', 'user__homepage', 'user__avatar')
    return JsonResponse({'data': list(answers)}, safe="false")

# def rate(request):
#     post_id = int(request.GET.get('post_id'))
#     value = int(request.GET.get('value'))
#     answers = Post.update_or_create(id=post_id, )
#     return JsonResponse({'data': list(answers)}, safe="false")


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

async def get_user_id(username):
    await User.objects.aget(username=username)
