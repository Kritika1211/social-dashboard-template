from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login

def register(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'register.html', {'form': form})