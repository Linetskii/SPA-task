"""Views for SPA"""
from datetime import datetime, timezone
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import ListView, View
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import MessageForm
from .models import User, Post
from django.utils.safestring import mark_safe


class IndexView(ListView):
    template_name = 'spa/index.html'
    model = Post
    paginate_by = 3

    def get_queryset(self):
        return super().get_queryset().prefetch_related("user").filter(prev_post=0)

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-date')
        return ordering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        context['ordering'] = self.get_ordering()
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
                    parent=(None if prev_post == 0 else Post.objects.get(id=prev_post)),
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
                        parent=(None if prev_post == 0 else Post.objects.get(id=prev_post)),
                    )
                    messages.add_message(request, messages.INFO, f"Message sended")

            return HttpResponseRedirect("")
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)


def answers(request):
    prev_post = int(request.GET.get('prev_post'))
    answers = Post.objects.prefetch_related("user").filter(prev_post=prev_post).values(
        'id', 'date', 'file', 'text', 'n_answers', 'user__username', 'user__email', 'user__homepage', 'user__avatar'
    )
    count = []
    for i in answers:
        count.append(Post.objects.filter(prev_post=i.get('id')).count())
    return JsonResponse({'data': list(answers)}, safe="false")
