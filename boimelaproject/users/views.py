from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm
from boimelawebApp.models import Book, Stall
# Create your views here.

# Python classes that have been created generate the html forms for us
# Most classes already exist so they need not be created from scratch


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    u_form = UserUpdateForm(request.POST, instance=request.user)
    if request.method == 'POST':

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Voila!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'profile.html', context)
