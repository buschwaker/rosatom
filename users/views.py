from django.contrib.auth.views import login as auth_views_login
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from .forms import SignUpForm


def my_login(*args, **kwargs):
    extra_context = {
        'urls': [
            '/',
        ]
    }
    return auth_views_login(*args, extra_context=extra_context, **kwargs)


@user_passes_test(lambda u: u.is_staff)
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:index')
        else:
            messages.error(request, 'Correct the errors below')
    else:
        form = SignUpForm()
    return render(request, 'users/login.html', {'form': form, 'register': 'True'})
