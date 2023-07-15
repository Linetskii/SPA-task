"""Views for SPA"""
from datetime import datetime, timezone
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import ListView
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
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
            c_form = form.cleaned_data
            username = c_form.get('username')
            password = c_form.get('password')
            prev_post = int(c_form.get('prev_post'))
            try:
                user_object = User.objects.get(username=username)
            except ObjectDoesNotExist:
                messages.add_message(request, messages.INFO, "Authorisation failed")
                user_object = None


            if user_object is None:
                User.objects.create(
                    username=c_form.get('username'),
                    email=c_form.get('email'),
                    homepage=c_form.get('homepage'),
                    avatar=c_form.get('avatar'),
                    password=c_form.get('password'),
                )
                user_id = User.objects.get(username=username).id
                Post.objects.create(
                    user_id=user_id,
                    date=datetime.now(tz=timezone.utc),
                    file=c_form.get('attachment'),
                    text=c_form.get('text'),
                    prev_post=prev_post,
                )
                messages.add_message(request, messages.INFO, f"Greetings, {username}!")
            else:
                if user_object.password == password:
                    user_id = User.objects.get(username=username).id
                    Post.objects.create(
                        user_id=user_id,
                        date=datetime.now(tz=timezone.utc),
                        file=c_form.get('attachment'),
                        text=c_form.get('text'),
                        prev_post=prev_post,
                    )
                    messages.add_message(request, messages.INFO, f"Message sended")

            return redirect('index')
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)


def answers(request):
    pp = int(request.GET.get('prev_post'))
    answers = Post.objects.prefetch_related("user").filter(prev_post=pp).values(
        'id', 'date', 'file', 'text', 'user__username', 'user__email', 'user__homepage', 'user__avatar'
    )
    return JsonResponse({'data': list(answers)}, safe="false")

# def send_message(request):